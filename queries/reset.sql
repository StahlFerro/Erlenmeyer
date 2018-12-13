DELETE FROM public.ship;
DELETE FROM public.ship_status;
DELETE FROM public.ship_type;
DELETE FROM public.engine;
DELETE FROM public.builder;
DELETE FROM public.user;
DELETE FROM public.revoked_token;

ALTER SEQUENCE ship_id_seq RESTART;
ALTER SEQUENCE ship_status_id_seq RESTART;
ALTER SEQUENCE ship_type_id_seq RESTART;
ALTER SEQUENCE engine_id_seq RESTART;
ALTER SEQUENCE builder_id_seq RESTART;
ALTER SEQUENCE user_id_seq RESTART;
ALTER SEQUENCE revoked_token_id_seq RESTART;
