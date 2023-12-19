SELECT 
    h.id,
    m.guid,
    m.text,
    m.reply_to_guid,
    m.thread_originator_guid,
    m.replace,
    m.associated_message_guid,
    m.date
FROM message as m
LEFT JOIN handle as h 
ON m.handle_id = h.ROWID
LEFT JOIN chat_message_join as cm
ON m.ROWID sage_id
LEFT JOIN chat as c
ON cm.chat_id = c.ROWID
WHERE (c.display_name = "L4 Software Engineers Only" OR c.display_name = "Software Engineers Only") AND NOT m.is_emote
ORDER BY m.date ASC;