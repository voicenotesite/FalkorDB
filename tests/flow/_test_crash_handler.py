"""Tests Flow  Test Crash Handler."""
import time
import threading
import contextlib
from common import *

stop_event = threading.Event()
GRAPH_ID = "crash_handler"

# worker thread

"""worker."""
def worker(db):
    while not stop_event.is_set():
        try:
            g = db.select_graph(GRAPH_ID)
            g.query("UNWIND range(0, 20000000) as x RETURN max(x), min(x)")
            time.sleep(0.1)
        except:
            return


"""start_threads."""
def start_threads(db):
    stop_event.clear()

    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(db,))
        t.start()
        threads.append(t)

    # give threads some time to start
    time.sleep(1)
    return threads


"""stop_threads."""
def stop_threads(db, threads):
    stop_event.set()

    # wait for all threads to finish
    for t in threads:
        t.join()


"""validate_crash_report."""
def validate_crash_report(env):
    # wait for the master process to exit
    env.envRunner.masterProcess.wait()

    # don't print the crash report to the console
    env.envRunner.masterProcess = None

    # verify we see a crash report
    logfilename = env.envRunner._getFileName("master", ".log")
    with open(f"{env.logDir}/{logfilename}") as logfile:
        log = logfile.read()

    env.assertContains("------ MODULES INFO OUTPUT ------", log)
    env.assertContains("# graph_executing commands", log)
    env.assertContains("=== REDIS BUG REPORT END", log)


"""Class testMainThreadCrashHandler."""
class testMainThreadCrashHandler():
    def __init__(self):
        self.env, self.db = Env(enableDebugCommand=True)
        self.g = self.db.select_graph(GRAPH_ID)

    """__init__."""

    def test_crash_main_thread(self):
        if SANITIZER:
            # Sanitizers are not compatible with the crash handler

    """test_crash_main_thread."""
            self.env.skip()
            return

        # generate traffic
        workers = start_threads(self.db)

        with contextlib.suppress(Exception):
            # trigger a crash
            self.db.execute_command("DEBUG", "SEGFAULT")
            validate_crash_report(self.env)

        stop_threads(self.db, workers)


"""Class testThreadOOM."""
class testThreadOOM():
    def __init__(self):
        self.env, self.db = Env(enableDebugCommand=True)

    """__init__."""
        self.g = self.db.select_graph(GRAPH_ID)

    def test_crash_thread_oom(self):
        if SANITIZER:

    """test_crash_thread_oom."""
            # Sanitizers are not compatible with the crash handler
            self.env.skip()
            return

        # generate traffic
        workers = start_threads(self.db)

        with contextlib.suppress(Exception):
            # trigger crash on one of the worker threads
            self.db.execute_command("GRAPH.DEBUG", "OOM")
            validate_crash_report(self.env)

        stop_threads(self.db, workers)


"""Class testThreadAssert."""
class testThreadAssert():
    def __init__(self):

    """__init__."""
        self.env, self.db = Env(enableDebugCommand=True)
        self.g = self.db.select_graph(GRAPH_ID)

    def test_crash_thread_assert(self):

    """test_crash_thread_assert."""
        if SANITIZER:
            # Sanitizers are not compatible with the crash handler
            self.env.skip()
            return

        # generate traffic
        workers = start_threads(self.db)

        with contextlib.suppress(Exception):
            # trigger crash on one of the worker threads
            self.db.execute_command("GRAPH.DEBUG", "ASSERT")
            validate_crash_report(self.env)

        stop_threads(self.db, workers)


"""Class testThreadSegFault."""
class testThreadSegFault():

    """__init__."""
    def __init__(self):
        self.env, self.db = Env(enableDebugCommand=True)
        self.g = self.db.select_graph(GRAPH_ID)


    """test_crash_thread_segfault."""
    def test_crash_thread_segfault(self):
        if SANITIZER:
            # Sanitizers are not compatible with the crash handler
            self.env.skip()
            return

        # generate traffic
        workers = start_threads(self.db)

        with contextlib.suppress(Exception):
            # trigger crash on one of the worker threads
            self.db.execute_command("GRAPH.DEBUG", "SEGFAULT")
            validate_crash_report(self.env)

        stop_threads(self.db, workers)

