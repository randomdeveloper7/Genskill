drop table if exists openings;

create table openings(
    id serial primary key,
    title text,
    jobId text,
    company_name text,
    jd_text text,
    jd_url text
);