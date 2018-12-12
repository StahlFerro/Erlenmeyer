--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.11
-- Dumped by pg_dump version 9.6.11

-- Started on 2018-12-12 10:33:41 WIB

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
-- TOC entry 2223 (class 0 OID 386347)
-- Dependencies: 193
-- Data for Name: builder; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.builder (name, code, date_founded, founder, headquarters) VALUES ('Kim Seah Shipyard', 'KSSI', '2000-01-22', 'Jimmy Walton', 'Indonesia');


--
-- TOC entry 2233 (class 0 OID 0)
-- Dependencies: 192
-- Name: builder_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.builder_id_seq', 1, true);


--
-- TOC entry 2221 (class 0 OID 386332)
-- Dependencies: 191
-- Data for Name: engine; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.engine (name, code, power_output, type) VALUES ('Westinghouse A2W', 'A2W', 150000, 'Nuclear');


--
-- TOC entry 2234 (class 0 OID 0)
-- Dependencies: 190
-- Name: engine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.engine_id_seq', 1, true);


--
-- TOC entry 2227 (class 0 OID 499431)
-- Dependencies: 197
-- Data for Name: ship_status; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ship_status ( name, description) VALUES ('Under construction', NULL);
INSERT INTO public.ship_status ( name, description) VALUES ('Active', NULL);
INSERT INTO public.ship_status ( name, description) VALUES ('Decommissioned', NULL);
INSERT INTO public.ship_status ( name, description) VALUES ('Museum', NULL);
INSERT INTO public.ship_status ( name, description) VALUES ('Scrapped', NULL);


--
-- TOC entry 2225 (class 0 OID 498473)
-- Dependencies: 195
-- Data for Name: ship_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ship_type (name) VALUES ('Aircraft Carrier');
INSERT INTO public.ship_type (name) VALUES ('Battlecruiser');
INSERT INTO public.ship_type (name) VALUES ('Battleship');
INSERT INTO public.ship_type (name) VALUES ('Light Cruiser');
INSERT INTO public.ship_type (name) VALUES ('Heavy Cruiser');
INSERT INTO public.ship_type (name) VALUES ('Destroyer');
INSERT INTO public.ship_type (name) VALUES ('Dreadnought');
INSERT INTO public.ship_type (name) VALUES ('Mine planter');
INSERT INTO public.ship_type (name) VALUES ('Submarine');
INSERT INTO public.ship_type (name) VALUES ('Corvette');
INSERT INTO public.ship_type (name) VALUES ('Frigate');
INSERT INTO public.ship_type (name) VALUES ('Missile boat');
INSERT INTO public.ship_type (name) VALUES ('Landing platform/dock');
INSERT INTO public.ship_type (name) VALUES ('Landing ship tank');
INSERT INTO public.ship_type (name) VALUES ('Hovercraft');
INSERT INTO public.ship_type (name) VALUES ('Hospital ship');
INSERT INTO public.ship_type (name) VALUES ('Research vessel');
INSERT INTO public.ship_type (name) VALUES ('Patrol vessel');
INSERT INTO public.ship_type (name) VALUES ('Ferry');
INSERT INTO public.ship_type (name) VALUES ('Yacht');
INSERT INTO public.ship_type (name) VALUES ('Motorboat');
INSERT INTO public.ship_type (name) VALUES ('Cruise ship');
INSERT INTO public.ship_type (name) VALUES ('Container');
INSERT INTO public.ship_type (name) VALUES ('Tanker');


--
-- TOC entry 2219 (class 0 OID 386322)
-- Dependencies: 189
-- Data for Name: ship; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('USS Enterprise', 'CV-65', 40, '1961-01-01', 40, 1, NULL, 1, NULL);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('Queen Star 3', '9VBQ5', 65, '2016-10-28', 60, NULL, 1, 19, NULL);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('Pegasus V', 'P5STE', 31, '2013-05-12', 12, NULL, NULL, 19, NULL);


--
-- TOC entry 2235 (class 0 OID 0)
-- Dependencies: 188
-- Name: ship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.ship_id_seq', 3, true);


--
-- TOC entry 2236 (class 0 OID 0)
-- Dependencies: 196
-- Name: ship_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.ship_status_id_seq', 5, true);


--
-- TOC entry 2237 (class 0 OID 0)
-- Dependencies: 194
-- Name: ship_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.ship_type_id_seq', 24, true);


--
-- TOC entry 2217 (class 0 OID 386313)
-- Dependencies: 187
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."user" (username, password_hash) VALUES ('admin', '$argon2i$v=19$m=102400,t=4,p=8$7b0X4nxvDaH03luL8R7jHOMcQwiBUIrxPmcsJUSoVeqdcy4lZEzJ2Q$7GWdamuppqqQqjBb9m1R+g');


--
-- TOC entry 2238 (class 0 OID 0)
-- Dependencies: 186
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

--SELECT pg_catalog.setval('public.user_id_seq', 1, true);


-- Completed on 2018-12-12 10:33:41 WIB

--
-- PostgreSQL database dump complete
--

