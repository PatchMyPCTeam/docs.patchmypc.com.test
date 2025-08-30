---
description: Details of the upgrade process
---

# Upgrading Insights

_Applies to: Patch My PC Advanced and Patch Insights_

To upgrade Advanced Insights, we need to re-run the installer using the latest version downloaded from [here](../download-and-install-insights/).&#x20;

{% hint style="info" %}
To upgrade silently please run AdvancedInsights.exe /q /l\*v %temp%\AdvInsights.log
{% endhint %}

When you run the installer, it will prompt for you to accept the license terms.

![](/_images/image-%281057%29.png-"Upgrade-license-terms" "")

You will be presented with the upgrade summary page. There is also the option to change the certificate, network port or IIS application pool identity if required.

![](/_images/vmconnect_1iGyaX71Gh.png-"Upgrade-Summary" "")

If upgrading from 1.0.x and 2.0.x versions of Advanced Insights, the upgrade summary page will also include summary information about the Advanced Insights SQL DB migration to SQLite.

See section: [upgrading-to-advanced-insights-2.1-and-later-from-1.0.x-and-2.0.x-versions.md](upgrading-to-advanced-insights-2.1-and-later-from-1.0.x-and-2.0.x-versions.md "mention")

If you wish to do so, click the **'View / Change Cert'** button will show additional information about any warnings being flagged.

![](/_images/image-%28707%29.png-"Existing-certificate-properties" "")

Following this, click **Install** to start the upgrade process.

The upgrade success page is displayed upon completion.

![](/_images/vmconnect_CClh8mYcG6.png-"Upgrade-Success-page" "")
