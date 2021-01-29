:- use_module(library('semweb/rdf_db'),
	[ rdf_split_url/3, rdf_meta/1 ]).
:- use_module(library('db/tripledb'),
    [ tripledb_load/2 ]).

:- tripledb_load(
        'package://knowrob_tiago_dual/owl/tiago_dual.owl',
        [ namespace(test)
        ]).