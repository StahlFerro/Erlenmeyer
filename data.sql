--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.11
-- Dumped by pg_dump version 9.6.11

-- Started on 2018-11-21 21:13:20 WIB

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
-- TOC entry 2203 (class 0 OID 386347)
-- Dependencies: 193
-- Data for Name: builder; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.builder (id, name, code, date_founded, founder, headquarters) VALUES (1, 'Kim Seah Shipyeard', 'KSSI', '2000-01-22', 'Jimmy Walton', 'Indonesia');


--
-- TOC entry 2209 (class 0 OID 0)
-- Dependencies: 192
-- Name: builder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.builder_id_seq', 1, false);


--
-- TOC entry 2201 (class 0 OID 386332)
-- Dependencies: 191
-- Data for Name: engine; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.engine (id, name, code, power_output, type) VALUES (1, 'Westinghouse A2W', 'A2W', 150000, 'Nuclear');


--
-- TOC entry 2210 (class 0 OID 0)
-- Dependencies: 190
-- Name: engine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.engine_id_seq', 1, false);


--
-- TOC entry 2199 (class 0 OID 386322)
-- Dependencies: 189
-- Data for Name: ship; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ship (id, name, code, speed, launch_date, capacity, engine_id, builder_id) VALUES (1, 'USS Enterprise', 'CV-65', 40, '1961-01-01', 40, 1, NULL);
INSERT INTO public.ship (id, name, code, speed, launch_date, capacity, engine_id, builder_id) VALUES (3, 'Pegasus V', 'P5STE', 31, '2013-05-12', 12, NULL, NULL);
INSERT INTO public.ship (id, name, code, speed, launch_date, capacity, engine_id, builder_id) VALUES (2, 'Queen Star 3', '9VBQ5', 65, '2016-10-28', 60, NULL, 1);


--
-- TOC entry 2211 (class 0 OID 0)
-- Dependencies: 188
-- Name: ship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ship_id_seq', 1, false);


--
-- TOC entry 2197 (class 0 OID 386313)
-- Dependencies: 187
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."user" (id, username, password_hash) VALUES (1, 'admin', 'pbkdf2:sha256:50000$ymEekEbS$a46f2298ce0a74e484dbce39b0b1f016c474f474e07837c457cdee90df1917f3');


--
-- TOC entry 2212 (class 0 OID 0)
-- Dependencies: 186
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 1, false);


-- Completed on 2018-11-21 21:13:20 WIB

--
-- PostgreSQL database dump complete
--

