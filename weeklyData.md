# Done Tickets

https://hlam-collab.atlassian.net/browse/DDS-39
The downtime was not working as expected, so we proposed another solution
Created Datadog downtime windows using monitor tags and configured for Uday’s windows

https://hlam-collab.atlassian.net/browse/DDS-51
Create multiple queues for the Jira tickets list

https://hlam-collab.atlassian.net/browse/DDS-6
Created a procedure to trace the error, fixed with the help of Dave

https://hlam-collab.atlassian.net/browse/DDS-53
Trace a dagster error

https://hlam-collab.atlassian.net/browse/DDS-12
Spidermail vs snowflake missmatch


https://hlam-collab.atlassian.net/browse/DDS-50
Adding some missing dataset grups in the datadog dashboard


https://hlam-collab.atlassian.net/browse/DDS-62
The issue was caused by a JWT token public key fingerprint mismatch due to a secret/key rotation happening outside the normal sync window, leading to authentication failures in Firehose → Snowflake streaming. 
It was resolved by manually re-syncing the rotated secret between Snowflake and the Spidermail DMS account using the Lambda sync process, after which alerts stopped; ongoing monitoring of weekly rotations was advised.

https://hlam-collab.atlassian.net/browse/DDS-30
Noisy alert for 5min which closed in the ticket.
Removed logging observability latency metric and validated Datadog entry, pending confirmation with Dave 
Created and got merge request approved for removing latency metric from codebase 

https://hlam-collab.atlassian.net/browse/DDS-28
Investigated spider mail and DMS-related alerts; added detailed context and email references into ticket 
Raised and discussed recurring “reading from source paused” alerts and gathered explanation from Iain 

https://hlam-collab.atlassian.net/browse/DDS-57
Analysed DBT run logs (37 min vs 1 hour) by transforming logs and extracting model-level data
Converted DBT logs into structured format (CSV → Excel) for analysis

Other
Checked June schedule email issue and followed up with owner
Reviewed and approved multiple merge requests and shared updates in channel
Identified model owner (Neil) for tax directive issue and initiated discussion

# Sessions

Knowledge connect - Reconciliation
- Discussion covered the ICMR data flow, including sources (Broker Focus and Recap), Snowflake processing, and how data is prepared and exposed to AutoRec.
- Team agreed to move away from Datadog dashboards to Sigma dashboards/alerts due to reliability issues and improve control over monitoring.
- Operational challenges (latency, data mismatches, reload processes, and fallback strategies) were reviewed, with proposals to streamline reloads and grant controlled access for quicker resolution.


# Pending Discussions
