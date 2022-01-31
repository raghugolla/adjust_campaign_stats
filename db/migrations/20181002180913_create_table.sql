-- migrate:up

CREATE TABLE campaign (
    id uuid PRIMARY KEY,
    campaign_date  timestamp with time zone NOT NULL,
    channel character varying(100) NOT NULL, -- assuming channel name is not more than 100 char
    country character varying(50) NOT NULL, -- assuming country name is not more than 50 char
    os character varying(20) NOT NULL, -- assuming os name is not more than 50 char
    impressions integer NOT NULL,
    clicks integer NOT NULL,
    installs integer NOT NULL,
    spend float NOT NULL,
    revenue float NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL
);
-- migrate:down

DROP TABLE public.campaign;
