---
description: >-
  Getting started with a Sync Schedule for the patch my pc publisher and
  understanding product timing.
---

# Sync Schedule

_Applies to: On-premises Publisher_

## Scheduling Daily Publish

By default, we recommend the Publisher sync runs on a daily basis. The sync schedule only controls <strong>when updates or applications are published</strong> to your environment. Keep in mind this will also affect assignment scheduling if you use the manage assignments feature.

<blockquote class="wp-block-quote">
<p><strong>Tip</strong>: Generally, Patch My PC releases an update to the catalog <strong>three to five times a week</strong>. These updates are released usually posted by <strong>4:00 PM Eastern Time</strong>.</p>
</blockquote>

When Patch My PC releases these new updates, the <strong>sync schedule is what automates the publication process</strong>.&#x20;

You can also manually start the sync and publication process at any time by selecting the <strong>Run Publishing Service Sync</strong> option.

![Publishing Daily Sync Options](/_images/image (1123).png>)

### Intune Application Manager

After the sync, you can view the published products with the [Intune Application Manager.](https://patchmypc.com/intune-application-manager-utility) This feature will provide you with a live view of all Win32 apps currently in your Intune tenant.&#x20;

It can help you:

* <strong>Export a list of your Intune Win32 apps to .csv</strong>, so you can use our [<strong>Power BI template</strong>](https://patchmypc.com/power-bi-reports-for-microsoft-intune-third-party-updates) to report on third party patching in Intune
* <strong>Manage live assignments</strong> for all of your existing Win32 apps in Intune
* <strong>Multi-select and delete</strong> Intune Win32 apps or their assignments

The utility can be found within the Publisher in either the <strong>Intune Apps</strong> or <strong>Intune Updates</strong> tab, on the right-hand side as a cloud icon with a magnifying glass:

![](/_images/image-(1122).png>)

Below is an example screenshot of what the utility looks like in a tenant with some Win32 apps. This is a <strong>live view of all Win32 apps</strong> currently in your tenant.

![](/_images/image-(1125).png>)