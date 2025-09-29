# Pause Cloud Updates

_Applies to: Patch My PC Cloud_

The _Pause Updates_ feature (which is disabled by default) of Patch My PC (PMPC) Cloud allows you to prevent an app that’s previously been successfully deployed from being updated whenever a new version is released.

<blockquote class="wp-block-quote is-important">
<p>Pausing updates for an app only affects our portal. If a new version of an app becomes available and updates are paused, the portal won’t create a new version of that app while updates are paused.</p>
<p>However, any existing versions of apps already in Intune that are assigned will still be evaluated and, if applicable, installed by your devices.</p>
</blockquote>

To Pause Updates for an app:

1. Click on the relevant successful deployment you want to pause for updates.

<blockquote class="wp-block-quote is-tip">
<p>Click the filter button (![](/_images/image-(2513).png>)) and select the **Disabled** option under the **Updates** section, followed by **Apply Filters** to see just those deployments that do not have updates paused.&#x20;</p>
</blockquote>

![Clicking on the relevant successful deployment you want to pause for updates](/_images/image-(1788).png "Clicking on the relevant successful deployment you want to pause for updates")

2.  Click the **Pause Updates** slider to enable it.\


    ![Clicking the "Pause Updates" slider](/_images/image-(1997).png "Clicking the “Pause Updates” slider")


3.  Click the **X** to close the deployment properties page.\


    ![Clicking "X" to close the deployment properties page.](/_images/image-(1998).png "Clicking &#x22;X&#x22; to close the deployment properties page.")

    \
    The list of deployments is displayed and **UPDATES PAUSED** shows under the deployment name so you updates are paused for this specific deployment.\


    ![](/_images/image-(1999).png)

<blockquote class="wp-block-quote is-note">
<p>If **Pause Updates** is enabled for an app and a newer version is available, the **Update Now** option will be available. See the [Update Now](sync-now-cloud-feature.md) process for more details.</p>
<p>Also, if your deployment has [Update Rings](../cloud-update-rings/) enabled and you experience a problem with any of the rings, **Pause Updates** prevents both an existing ring from being upgraded to a new version and any additional Update Rings from being created provided the **Immediate** option was set for the rings.</p>
<p>The **Pause Updates** option will be unavailable if your deployment uses **Delayed** rings and some of these rings have yet to update. As a workaround, you can delete the deployment to stop any outstanding updates.</p>
</blockquote>