--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.11
-- Dumped by pg_dump version 9.6.11

-- Started on 2018-11-23 13:17:06 WIB

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
--SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 2213 (class 0 OID 386347)
-- Dependencies: 193
-- Data for Name: builder; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.builder (id, name, code, date_founded, founder, headquarters) VALUES (1, 'Kim Seah Shipyard', 'KSSI', '2000-01-22', 'Jimmy Walton', 'Indonesia');


--
-- TOC entry 2221 (class 0 OID 0)
-- Dependencies: 192
-- Name: builder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.builder_id_seq', 1, false);


--
-- TOC entry 2211 (class 0 OID 386332)
-- Dependencies: 191
-- Data for Name: engine; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.engine (id, name, code, power_output, type) VALUES (1, 'Westinghouse A2W', 'A2W', 150000, 'Nuclear');


--
-- TOC entry 2222 (class 0 OID 0)
-- Dependencies: 190
-- Name: engine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.engine_id_seq', 1, false);


--
-- TOC entry 2215 (class 0 OID 498473)
-- Dependencies: 195
-- Data for Name: ship_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ship_type (id, name) VALUES (1, 'Aircraft Carrier');
INSERT INTO public.ship_type (id, name) VALUES (2, 'Battlecruiser');
INSERT INTO public.ship_type (id, name) VALUES (3, 'Battleship');
INSERT INTO public.ship_type (id, name) VALUES (4, 'Light Cruiser');
INSERT INTO public.ship_type (id, name) VALUES (5, 'Heavy Cruiser');
INSERT INTO public.ship_type (id, name) VALUES (6, 'Destroyer');
INSERT INTO public.ship_type (id, name) VALUES (7, 'Dreadnought');
INSERT INTO public.ship_type (id, name) VALUES (8, 'Mine planter');
INSERT INTO public.ship_type (id, name) VALUES (9, 'Submarine');
INSERT INTO public.ship_type (id, name) VALUES (10, 'Corvette');
INSERT INTO public.ship_type (id, name) VALUES (11, 'Frigate');
INSERT INTO public.ship_type (id, name) VALUES (12, 'Missile boat');
INSERT INTO public.ship_type (id, name) VALUES (14, 'Landing platform/dock');
INSERT INTO public.ship_type (id, name) VALUES (15, 'Landing ship tank');
INSERT INTO public.ship_type (id, name) VALUES (16, 'Hovercraft');
INSERT INTO public.ship_type (id, name) VALUES (17, 'Hospital ship');
INSERT INTO public.ship_type (id, name) VALUES (18, 'Research vessel');
INSERT INTO public.ship_type (id, name) VALUES (13, 'Patrol vessel');
INSERT INTO public.ship_type (id, name) VALUES (19, 'Ferry');
INSERT INTO public.ship_type (id, name) VALUES (20, 'Yacht');
INSERT INTO public.ship_type (id, name) VALUES (21, 'Motorboat');
INSERT INTO public.ship_type (id, name) VALUES (22, 'Cruise ship');
INSERT INTO public.ship_type (id, name) VALUES (23, 'Container');
INSERT INTO public.ship_type (id, name) VALUES (24, 'Tanker');


--
-- TOC entry 2209 (class 0 OID 386322)
-- Dependencies: 189
-- Data for Name: ship; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ship (id, name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id) VALUES (1, 'USS Enterprise', 'CV-65', 40, '1961-01-01', 40, 1, NULL, 1);
INSERT INTO public.ship (id, name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id) VALUES (2, 'Queen Star 3', '9VBQ5', 65, '2016-10-28', 60, NULL, 1, 19);
INSERT INTO public.ship (id, name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id) VALUES (3, 'Pegasus V', 'P5STE', 31, '2013-05-12', 12, NULL, NULL, 19);


--
-- TOC entry 2223 (class 0 OID 0)
-- Dependencies: 188
-- Name: ship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ship_id_seq', 1, false);


--
-- TOC entry 2224 (class 0 OID 0)
-- Dependencies: 194
-- Name: ship_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ship_type_id_seq', 1, false);


--
-- TOC entry 2207 (class 0 OID 386313)
-- Dependencies: 187
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."user" (id, username, password_hash) VALUES (1, 'admin', 'pbkdf2:sha256:50000$ymEekEbS$a46f2298ce0a74e484dbce39b0b1f016c474f474e07837c457cdee90df1917f3');


--
-- TOC entry 2225 (class 0 OID 0)
-- Dependencies: 186
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 1, false);


-- Completed on 2018-11-23 13:17:06 WIB

--
-- PostgreSQL database dump complete
--
