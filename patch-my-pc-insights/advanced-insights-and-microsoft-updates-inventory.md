---
description: Advanced Insights Update scanning (this is not relevant for Patch Insights)
---

# Advanced Insights and Microsoft Updates Inventory

_Applies to: Patch My PC Advanced Insights_

If you use <strong>Intune</strong> to manage your windows updates (<strong>Windows Update for Business</strong>) then none of that compliance data is visible from ConfigMgr. This requires you to have to read compliance data from BOTH ConfigMgr and Intune.

## Solution

* You get <strong>complete</strong> visibility of <strong>all</strong> update compliance from Advanced Insights

![](/_images/Microsoft-Updates-Page.png)

<strong>*

## How does it work?

We supplement your ConfigMgr compliance data with </strong>additional data<strong> from Microsoft Update.

Our Inventory Extensions WMI Provider runs on clients and scans against Microsoft Update to find update compliance data. This data is then pulled into ConfigMgr via Hardware Inventory for reporting.

![](/_images/image-(1308).png "")

</strong>*

## Requirements

1. You must complete the implementation steps in the [Configuration Guide](advanced-insights-inventory-extensions/)
2. Clients must be configured to use <strong>Windows Update for Business</strong>