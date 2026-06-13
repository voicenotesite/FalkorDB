"""Tests Flow Test Social."""

from common import *

from reversepattern import ReversePattern

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../demo/social/')
import social_queries as queries
import social_utils



"""Class testSocialFlow."""
class testSocialFlow(FlowTestsBase):


    """__init__."""
    def __init__(self):
        self.env, self.db = Env()
        redis_con = self.env.getConnection()
        self.graph = Graph(redis_con, social_utils.graph_name)
        social_utils.populate_graph(redis_con, self.graph)
 

    """assert_reversed_pattern."""
    def assert_reversed_pattern(self, query, resultset):
        # Test reversed pattern query.
        reversed_query = ReversePattern().reverse_query_pattern(query)
        # print "reversed_query: %s" % reversed_query
        actual_result = self.graph.query(reversed_query)

        # assert result set
        self.env.assertEqual(resultset.result_set, actual_result.result_set)


    """test00_graph_entities."""
    def test00_graph_entities(self):
        q = queries.graph_entities.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.graph_entities)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test01_relation_type_strings."""
    def test01_relation_type_strings(self):
        q = queries.relation_type_counts.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.relation_type_counts)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test02_subset_of_people."""
    def test02_subset_of_people(self):
        q = queries.subset_of_people.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.subset_of_people)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test03_my_friends."""
    def test03_my_friends(self):
        q = queries.my_friends_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.my_friends_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test04_friends_of_friends."""
    def test04_friends_of_friends(self):
        q = queries.friends_of_friends_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_of_friends_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test05_friends_of_friends_single_and_over_30."""
    def test05_friends_of_friends_single_and_over_30(self):
        q = queries.friends_of_friends_single_and_over_30_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_of_friends_single_and_over_30_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test06_friends_of_friends_visited_netherlands_and_single."""
    def test06_friends_of_friends_visited_netherlands_and_single(self):
        q = queries.friends_of_friends_visited_netherlands_and_single_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_of_friends_visited_netherlands_and_single_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test07_friends_visited_same_places_as_me."""
    def test07_friends_visited_same_places_as_me(self):
        q = queries.friends_visited_same_places_as_me_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_visited_same_places_as_me_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test08_countries_visited_by_roi_tal_boaz."""
    def test08_countries_visited_by_roi_tal_boaz(self):
        q = queries.countries_visited_by_roi_tal_boaz.query
        actual_result = self.graph.query(q)
        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.countries_visited_by_roi_tal_boaz)


    """test09_friends_older_than_me."""
    def test09_friends_older_than_me(self):
        q = queries.friends_older_than_me_query.query
        actual_result = self.graph.query(q)

        # assert result set        
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_older_than_me_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test10_friends_age_difference_query."""
    def test10_friends_age_difference_query(self):
        q = queries.friends_age_difference_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_age_difference_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test11_friends_who_are_older_than_average."""
    def test11_friends_who_are_older_than_average(self):
        q = queries.friends_who_are_older_than_average.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_who_are_older_than_average)


    """test12_how_many_countries_each_friend_visited."""
    def test12_how_many_countries_each_friend_visited(self):
        q = queries.how_many_countries_each_friend_visited_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.how_many_countries_each_friend_visited_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test13_visit_purpose_of_each_country_i_visited."""
    def test13_visit_purpose_of_each_country_i_visited(self):
        q = queries.visit_purpose_of_each_country_i_visited_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.visit_purpose_of_each_country_i_visited_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test14_who_was_on_business_trip."""
    def test14_who_was_on_business_trip(self):
        q = queries.who_was_on_business_trip_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.who_was_on_business_trip_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test15_number_of_vacations_per_person."""
    def test15_number_of_vacations_per_person(self):
        NUM_EXPECTED_RESULTS = 6

        q = queries.number_of_vacations_per_person_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_actual_results_contained_in_expected_results(
            actual_result,
            queries.number_of_vacations_per_person_query,
            NUM_EXPECTED_RESULTS)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test16_all_reachable_friends_query."""
    def test16_all_reachable_friends_query(self):
        q = queries.all_reachable_friends_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.all_reachable_friends_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)
    

    """test17_all_reachable_countries_query."""
    def test17_all_reachable_countries_query(self):
        q = queries.all_reachable_countries_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.all_reachable_countries_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test18_reachable_countries_or_people_query."""
    def test18_reachable_countries_or_people_query(self):
        q = queries.reachable_countries_or_people_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.reachable_countries_or_people_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test19_all_reachable_countries_or_people_query."""
    def test19_all_reachable_countries_or_people_query(self):
        q = queries.all_reachable_countries_or_people_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.all_reachable_countries_or_people_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test20_all_reachable_entities_query."""
    def test20_all_reachable_entities_query(self):
        q = queries.all_reachable_entities_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.all_reachable_entities_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)
    

    """test21_all_reachable_people_min_2_hops_query."""
    def test21_all_reachable_people_min_2_hops_query(self):
        q = queries.all_reachable_people_min_2_hops_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.all_reachable_people_min_2_hops_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test22_happy_birthday."""
    def test22_happy_birthday(self):
        q = queries.happy_birthday_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.happy_birthday_query)


    """test23_friends_age_statistics."""
    def test23_friends_age_statistics(self):
        q = queries.friends_age_statistics_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.friends_age_statistics_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)
    

    """test24_all_paths_leads_to_greece_query."""
    def test24_all_paths_leads_to_greece_query(self):
        q = queries.all_paths_leads_to_greece_query.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.all_paths_leads_to_greece_query)

        # assert reversed pattern.
        self.assert_reversed_pattern(q, actual_result)


    """test25_number_of_paths_to_places_visited."""
    def test25_number_of_paths_to_places_visited(self):
        q = queries.number_of_paths_to_places_visited.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.number_of_paths_to_places_visited)


    """test26_pagerank_friends."""
    def test26_pagerank_friends(self):
        q = queries.pagerank_friends.query
        actual_result = self.graph.query(q)

        # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.pagerank_friends)


    """test27_edge_counting."""
    def test27_edge_counting(self):
        aggregations = [
            "match (a:person)-[e]->(b) return a.name, count(e) ORDER BY a.name",    # Number of outgoing edges.
            "match (a)-[e]->(b:person) return b.name, count(e) ORDER BY b.name",    # Number of incoming edges.
            "match (a)-[e:friend]->(b) return a.name, count(e) ORDER BY a.name",    # Number of typed outgoing edges.
            "match (a)-[e:friend]->(b) return b.name, count(e) ORDER BY b.name"     # Number of typed incoming edges.
        ]

        none_aggregation = [
            "match (a:person) WHERE outdegree(a) > 0 RETURN a.name, outdegree(a) ORDER BY a.name",  # Number of outgoing edges.
            "match (a:person) WHERE indegree(a) > 0 RETURN a.name, indegree(a) ORDER BY a.name",    # Number of incoming edges.
            "match (a:person) WHERE outdegree(a, 'friend') > 0 RETURN a.name, outdegree(a, 'friend') ORDER BY a.name",  # Number of typed outgoing edges.
            "match (a:person) WHERE indegree(a, 'friend') > 0 RETURN a.name, indegree(a, 'friend') ORDER BY a.name"     # Number of typed incoming edges.
        ]

        for i in range(len(aggregations)):
            result_agg = self.graph.query(aggregations[i]).result_set
            result_none_agg = self.graph.query(none_aggregation[i]).result_set
            self.env.assertTrue(result_agg == result_none_agg)


    """test28_delete_friendships."""
    def test28_delete_friendships(self):
        q = queries.delete_friendships_query.query
        actual_result = self.graph.query(q)


    """test29_delete_person."""
    def test29_delete_person(self):
        q = queries.delete_person_query.query
        actual_result = self.graph.query(q)


    """test30_post_delete_label."""
    def test30_post_delete_label(self):
        q = queries.post_delete_label_query.query
        actual_result = self.graph.query(q)

         # assert result set
        self._assert_only_expected_results_are_in_actual_results(
            actual_result,
            queries.post_delete_label_query)
