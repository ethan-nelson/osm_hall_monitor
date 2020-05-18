DELETE FROM      history_users      WHERE TO_TIMESTAMP(timestamp, "YYYY-MM-DDTHH:MI:SSZ") < NOW() - INTERVAL '30 days';
DELETE FROM    history_all_users    WHERE TO_TIMESTAMP(timestamp, "YYYY-MM-DDTHH:MI:SSZ") < NOW() - INTERVAL '30 days';
DELETE FROM  history_users_objects  WHERE TO_TIMESTAMP(timestamp, "YYYY-MM-DDTHH:MI:SSZ") < NOW() - INTERVAL '30 days';
DELETE FROM     history_objects     WHERE TO_TIMESTAMP(timestamp, "YYYY-MM-DDTHH:MI:SSZ") < NOW() - INTERVAL '30 days';
DELETE FROM      history_keys       WHERE TO_TIMESTAMP(timestamp, "YYYY-MM-DDTHH:MI:SSZ") < NOW() - INTERVAL '30 days';
