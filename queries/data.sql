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
INSERT INTO public.builder (name, code, date_founded, founder, headquarters) VALUES ('Meyer Werft GmBH & Co. KG', 'MWRF', '1795-01-01', 'Willm Rolf Meyer', 'Germany');
INSERT INTO public.builder (name, code, date_founded, founder, headquarters) VALUES ('Newport News Shipbuilding', 'NNS', '1886-01-01', 'Collis Potter Huntington', 'United States');
INSERT INTO public.builder (name, code, date_founded, founder, headquarters) VALUES ('Kure Naval Arsenal', 'KNA', '1889-01-01', 'Imperial Japanese Navy', 'Japan');
INSERT INTO public.builder (name, code, date_founded, founder, headquarters) VALUES ('PT Penataran Angkatan Laut', 'PAL', '1939-01-01', 'Indonesia Ministry of SOEs', 'Indonesia');


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
INSERT INTO public.engine (name, code, power_output, type) VALUES ('Kampon Steam Boilers', 'KMP', 110000, 'Steam');
INSERT INTO public.engine (name, code, power_output, type) VALUES ('Wärtsilä 12V46F', 'WVF', 14400, 'Diesel-Electric');
INSERT INTO public.engine (name, code, power_output, type) VALUES ('SEMT Pielstick 20PA6B STC', 'SP2S', 8910, 'Diesel-Electric');


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

INSERT INTO public.ship_status (name, description) VALUES ('Under construction', 'The vessel is being developed and is not completed yet');
INSERT INTO public.ship_status (name, description) VALUES ('Active', 'Currently operating within its service');
INSERT INTO public.ship_status (name, description) VALUES ('Inactive', 'The vessel has its fuel, fluids and tools removed, alongside discharging the electrical system');
INSERT INTO public.ship_status (name, description) VALUES ('Decommissioned', 'Withdrawn from its active service');
INSERT INTO public.ship_status (name, description) VALUES ('Museum', 'Vessel permanently stationed and repurposed into a museum');
INSERT INTO public.ship_status (name, description) VALUES ('Scrapped', 'Disposed or dissasembled for scrap parts');
INSERT INTO public.ship_status (name, description) VALUES ('Sunk', 'Destroyed either in combat warfare, purposely disposed or sunk from an accident');


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

INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('USS Enterprise', 'CV-65', 33.6, '1961-01-01', 40, 1, 3, 1, 4);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('Queen Star 3', '9VBQ5', 39, '2016-10-28', 60, NULL, 1, 19, NULL);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('Pegasus V', 'P5STE', 31, '2013-05-12', 12, NULL, NULL, 19, 2);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('IJN Yamato', 'YMT', 27, '1940-08-08', 120, 2, 4, 3, 7);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('Anthem of the Seas', 'Q2RCI', 22, '2015-02-21', 4905, 3, 2, 22, 2);
INSERT INTO public.ship (name, code, speed, launch_date, capacity, engine_id, builder_id, ship_type_id, ship_status_id) VALUES ('KRI Raden Eddy Martadinata', 'RE331', 28, '2016-01-18', 35, 4, 5, 11, 2);


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

INSERT INTO public."user" (username, password_hash, client_secret, is_admin, date_created)
VALUES ('admin', '$argon2i$v=19$m=102400,t=4,p=8$7b0X4nxvDaH03luL8R7jHOMcQwiBUIrxPmcsJUSoVeqdcy4lZEzJ2Q$7GWdamuppqqQqjBb9m1R+g',
'TZxzkDo_Cm37NVwczcD0L2BxucvjXhX1XQzAdQA4OwYn_4eD-r80B8WUb4psINhoXUxTtiK2TzQN0WwOlRYWwg', TRUE, (now() at time zone 'utc'));
INSERT INTO public."user" (username, password_hash, client_secret, is_admin, date_created)
VALUES ('root', '$argon2i$v=19$m=102400,t=4,p=8$qJWSslbK2ftfi3HOee89hzBmLIWQspaScm7NuVfqHYOwdu4dI0QoxQ$saWPzOm14GtsFiHLvXfbHA',
'9pJJmF0OC6RlkX0odsEaVW9nxl8Z7eu30aEmf3nWy2fyFRy1Re8d5Bvku1fmwbqcSywK7sFhDlkhc7w14ZH2fw', TRUE, (now() at time zone 'utc'));
INSERT INTO public."user" (username, password_hash, client_secret, is_admin, date_created)
VALUES ('123', '$argon2i$v=19$m=102400,t=4,p=8$lZLSuveecy4l5Hzv/X9vbc2ZkzJGyFnrPUeIsRZCKKUUwpgzhvA+Zw$byHcgN8CyALeTzlxVcPKow',
'Punk_82l8AGsBDmBsE_CZBPISGZT_idg3yQq1qK1o_HPXYGTo3cpxqejDBGqUWJbqZtB-37SBOuQbhuYKh6I1w', FALSE, (now() at time zone 'utc'));

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

