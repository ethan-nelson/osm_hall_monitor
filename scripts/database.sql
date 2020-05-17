CREATE TABLE blocked_users (
    id SERIAL NOT NULL PRIMARY KEY,
    blockee text,
    blocker text,
    begindate timestamp with time zone,
    enddate timestamp with time zone,
    reason text
);

CREATE TABLE file_list (
    id SERIAL NOT NULL NOT NULL PRIMARY KEY,
    sequence text,
    "timestamp" text,
    timetype text,
    read boolean
);

CREATE TABLE history_all_changesets (
    id SERIAL NOT NULL PRIMARY KEY,
    changeset text NOT NULL,
    username text NOT NULL,
    "timestamp" text NOT NULL,
    created text,
    modified text,
    deleted text
);

CREATE TABLE history_all_users (
    id SERIAL NOT NULL PRIMARY KEY,
    username text NOT NULL,
    changeset text NOT NULL,
    "timestamp" text NOT NULL,
    created text,
    modified text,
    deleted text
);

CREATE TABLE history_filters (
    id SERIAL NOT NULL PRIMARY KEY,
    flag integer NOT NULL,
    username text NOT NULL,
    changeset bigint NOT NULL,
    "timestamp" text NOT NULL,
    quantity text NOT NULL,
    authorid bigint
);

CREATE TABLE history_keys (
    id SERIAL NOT NULL PRIMARY KEY,
    key text NOT NULL,
    value text NOT NULL,
    username text NOT NULL,
    changeset bigint NOT NULL,
    "timestamp" text NOT NULL,
    wid integer,
    userid bigint,
    element text,
    action smallint
);

CREATE TABLE history_objects (
    id SERIAL NOT NULL PRIMARY KEY,
    username text NOT NULL,
    changeset bigint NOT NULL,
    "timestamp" text NOT NULL,
    wid integer,
    userid bigint,
    action smallint
);

CREATE TABLE history_users (
    id SERIAL NOT NULL PRIMARY KEY,
    changeset bigint NOT NULL,
    "timestamp" text NOT NULL,
    created bigint,
    modified bigint,
    deleted bigint,
    wid integer,
    userid bigint
);

CREATE TABLE history_users_objects (
    id SERIAL NOT NULL PRIMARY KEY,
    key text NOT NULL,
    value text NOT NULL,
    username text NOT NULL,
    changeset bigint NOT NULL,
    "timestamp" text NOT NULL,
    action text
);

CREATE TABLE registered_users (
    id bigint NOT NULL PRIMARY KEY,
    username text,
    role integer
);

CREATE TABLE unblocked_users (
    id bigint NOT NULL PRIMARY KEY,
    username text,
    date_expired text
);

CREATE TABLE watched_keys (
    id SERIAL NOT NULL PRIMARY KEY,
    key text NOT NULL,
    value text NOT NULL,
    reason text,
    author text,
    email text,
    authorid bigint
);

CREATE TABLE watched_objects (
    id SERIAL NOT NULL PRIMARY KEY,
    element text NOT NULL,
    reason text,
    author text,
    email text,
    authorid bigint
);

CREATE TABLE watched_users (
    id SERIAL NOT NULL PRIMARY KEY,
    username text NOT NULL,
    reason text,
    author text,
    email text,
    authorid bigint
);

CREATE TABLE watched_users_objects (
    id SERIAL NOT NULL PRIMARY KEY,
    username text NOT NULL,
    reason text,
    author text,
    email text
);

CREATE TABLE whitelisted_users (
    id SERIAL NOT NULL PRIMARY KEY,
    username text NOT NULL,
    reason text,
    author text,
    authorid bigint
);
