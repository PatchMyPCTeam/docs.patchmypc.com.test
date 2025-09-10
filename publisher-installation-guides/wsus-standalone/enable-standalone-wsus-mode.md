---
description: This guide will walk through enabling Standalone WSUS Mode in the Publisher.
---

# Enable Standalone WSUS Mode

_Applies to: On-premises Publisher_

To enable standalone WSUS mode, go to the <strong>Updates</strong> tab and select <strong>Options</strong>. In the <strong>WSUS options</strong> window check the box <strong>Make updates appear in the WSUS console. This option isn’t needed if using Configuration Manager.</strong>

![](/_images/image-(1242).png>)

If your WSUS database is using a <strong>Windows Internal Database</strong> (WID), the <strong>database connection options will be read-only</strong>.

When using a <strong>SQL Server for the WSUS database</strong>, you will need to choose either to connect to the database using the <strong>SYSTEM account</strong> or define a user name and password using <strong>SQL authentication</strong>.

![](/_images/image-(1218).png>)

For more information on the minimum permissions required, please visit [our KB article](https://patchmypc.com/configuring-standalone-wsus-mode).