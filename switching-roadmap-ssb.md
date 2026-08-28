# Current Role Inventory

## A. Technologies

### Data Platform & Warehousing
- Snowflake
  - RBAC (Role-Based Access Control)
  - Database Roles
  - Masking Policies
  - Data Classification & Tags
  - Account Usage Views
  - Query Investigation
  - Access Management
  - Semantic Views
  - Data Governance
  - Metadata Management
  - Sigma Integration

### Cloud & Infrastructure
- AWS
  - DMS (Database Migration Service)
  - S3
  - IAM
  - Cloud Infrastructure Support

### Infrastructure as Code
- Terraform
  - Snowflake Resource Management
  - Access Automation
  - Environment Configuration

### Data Engineering
- SQL
- DBT
- Data Pipelines
- Data Modelling
- ETL / ELT Support

### Monitoring & Observability
- Datadog
- Grafana
- Platform Monitoring
- Alerting
- Cost Monitoring

### Development & Automation
- Python
- Streamlit
- Git
- GitLab
- CI/CD Pipelines
- Shell Scripting

### Service Management & Collaboration
- Jira
- ServiceNow
- Confluence
- Microsoft Teams

---

## B. Responsibilities

### Production Support
- Incident troubleshooting
- Production support
- Application support
- Deployment support
- Environment support
- Release validation

### Investigation & Analysis
- Issue investigation
- Root-cause analysis
- Log analysis
- Query investigation
- Data validation
- Performance troubleshooting

### Snowflake Administration
- Role and permission management
- User access management
- Database role administration
- Masking policy implementation
- Tag and classification management
- Object visibility troubleshooting

### Data Platform Operations
- Pipeline monitoring
- Pipeline recovery and reprocessing
- DMS task monitoring
- Schema updates
- Access provisioning
- Platform health checks

### Service Delivery
- Ticket handling
- Incident management
- Problem management
- Change implementation
- SLA adherence
- Escalation handling

### Communication & Documentation
- Client communication
- Stakeholder management
- Technical discussions
- Knowledge transfer
- Runbook creation
- Documentation maintenance

### Automation & Continuous Improvement
- Support automation
- Reporting automation
- Operational tooling development
- Process optimisation
- Monitoring improvements
- Platform reliability improvements

---

## C. Problems You've Solved

### Snowflake Permission Management

**Problem**  
Users required access to Snowflake data sources but lacked appropriate permissions.

**Investigation**  
Reviewed existing roles, access requirements, approval process and audit requirements.

**Solution**  
Created merge requests, implemented role assignments and validated access paths.

**Result**  
Users received required access while maintaining governance and audit compliance. 【1-455514】

---

### Sigma User Access Failure

**Problem**  
A user lost access after an email address change created a duplicate Sigma account.

**Investigation**  
Analysed SCIM provisioning behaviour and tested account update workflows.

**Solution**  
Mapped the correct email address to the existing permission-bearing account and removed the duplicate account conflict.

**Result**  
User access was restored without loss of permissions. 【1-455514】

---

### Streamlit Administration Tool Defect

**Problem**  
A Streamlit application failed during Sigma email update operations.

**Investigation**  
Reviewed application logs and code behaviour to identify failure points.

**Solution**  
Removed invalid rerun logic and corrected email handling functionality.

**Result**  
Successfully updated users without impacting existing permissions or access. 【1-455514】

---

### Production Pipeline Failures

**Problem**  
Data pipelines and platform services experienced failures impacting users.

**Investigation**  
Analysed logs, platform alerts, permissions and pipeline execution states.

**Solution**  
Restarted failed processes, corrected permissions, reprocessed workloads and escalated where required.

**Result**  
Platform services were restored and user impact was minimised. 【2-75b1cf】

---

### Masking Policy Deployment Risk

**Problem**  
Masking policy changes required validation before production deployment.

**Investigation**  
Reviewed policy behaviour, release scope and potential security implications.

**Solution**  
Scheduled dedicated testing and validation activities before release.

**Result**  
Reduced risk of incorrect data exposure and improved deployment confidence. 【1-455514】

---

## D. Achievements

### Automation

- Automated repetitive support and reporting workflows using Python, significantly reducing manual effort and improving consistency.
- Developed Streamlit-based administration tools to simplify Sigma and platform support activities. 【1-455514】

### Snowflake Platform Support

- Managed Snowflake RBAC, user provisioning, masking policies and data governance controls across multiple environments.
- Resolved complex permission and visibility issues while maintaining compliance and audit requirements. 【2-75b1cf】【1-455514】

### Incident Management

- Investigated and resolved production incidents involving Snowflake, data pipelines and platform services, helping maintain operational stability. 【2-75b1cf】

### Process Improvement

- Contributed to defining and improving the Data Teams Support Model, including responsibilities, escalation paths, monitoring practices and operational processes. 【2-75b1cf】

### Stakeholder Collaboration

- Worked closely with engineers, architects, analysts and business stakeholders to deliver platform support and access management solutions. 【1-455514】【2-75b1cf】

### Knowledge Sharing

- Produced operational documentation, runbooks and troubleshooting guidance to improve support effectiveness and reduce incident resolution times. 【2-75b1cf】

---

## Professional Summary

Data Platform & Production Support Consultant with hands-on experience supporting Snowflake, AWS, Sigma and enterprise data platforms. Skilled in incident management, root-cause analysis, access management, automation, monitoring and operational support. Experienced in developing Python and Streamlit solutions to improve platform operations, reduce manual effort and enhance support efficiency. 【2-75b1cf】【1-455514】
