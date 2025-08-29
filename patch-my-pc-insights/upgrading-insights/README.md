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

<figure><img src="../../_images/gitbook/image%20%281057%29.png" alt=""><figcaption><p>Upgrade license terms</p></figcaption></figure>

You will be presented with the upgrade summary page. There is also the option to change the certificate, network port or IIS application pool identity if required.

<figure><img src="../../_images/gitbook/vmconnect_1iGyaX71Gh.png" alt=""><figcaption><p>Upgrade Summary</p></figcaption></figure>

If upgrading from 1.0.x and 2.0.x versions of Advanced Insights, the upgrade summary page will also include summary information about the Advanced Insights SQL DB migration to SQLite.

See section: [upgrading-to-advanced-insights-2.1-and-later-from-1.0.x-and-2.0.x-versions.md](upgrading-to-advanced-insights-2.1-and-later-from-1.0.x-and-2.0.x-versions.md "mention")

If you wish to do so, click the **'View / Change Cert'** button will show additional information about any warnings being flagged.

<figure><img src="../../_images/gitbook/image%20%28707%29.png" alt=""><figcaption><p>Existing certificate properties</p></figcaption></figure>

Following this, click **Install** to start the upgrade process.

The upgrade success page is displayed upon completion.

<figure><img src="../../_images/gitbook/vmconnect_CClh8mYcG6.png" alt=""><figcaption><p>Upgrade Success page</p></figcaption></figure>
