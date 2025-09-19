# Resume Cloud Updates

_Applies to: Patch My PC Cloud_

If the _Pause Updates_ feature of Patch My PC (PMPC) Cloud has been configured for an app that has since been updated, and you want to bring the app up-to-date to the latest version, you need to disable pause updates.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If an app has more than one version of an update available, resuming updates will ensure it is updated to the latest version.</p>
<p>Also, if you paused a deployment with [Update Rings](../cloud-update-rings/) enabled, when you resume updates for that deployment, the Update Rings are re-enabled and function normally.</p>
</blockquote>

To resume updates for an app:

1. Click on the relevant deployment that has been paused.

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>Click the filter button (![](/_images/image-(2513).png>)) and select the <strong>Enabled</strong> option under the <strong>Updates</strong> section, followed by <strong>Apply Filters</strong> to see just those deployments that have updates paused.&#x20;</p>
</blockquote>

![Clicking on the relevant successful deployment which has been paused for updates](/_images/image-(2000).png "Clicking on the relevant successful deployment which has been paused for updates")

2.  Click the <strong>Pause Updates</strong> slider to disable it.\


    ![Clicking the “Pause Updates” slider](/_images/image-(2001).png "Clicking the “Pause Updates” slider")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Notice on the above screenshot that the <strong>Sync Now</strong> button is available, meaning one or more updates are available for this app.</p>
</blockquote>

3.  Click the <strong>X</strong> to close the deployment properties page.\


    ![Clicking “X” to close the deployment properties page](/_images/image-(2002).png "Clicking “X” to close the deployment properties page")

    \
    The list of deployments is displayed without <strong>UPDATES PAUSED</strong> under the deployment you just unpaused.\


    ![&#x22;UPDATES PAUSED&#x22; no longer under the deployment name.](/_images/image-(2003).png "&#x22;UPDATES PAUSED&#x22; no longer under the deployment name.")

Updates for this app are now resumed.

You now need to decide how you want to install any updates for this app:

* <strong>Install the updates now –</strong> If you want to install the updates as soon as possible, follow the [Sync Now](sync-now-cloud-feature.md) process.
* <strong>Wait for the nightly sync to run –</strong> If you are happy to wait for the updates to be installed the next time the daily sync runs (at 2 am by default), you do not need to do anything.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>You can change the Sync Schedule to a different time, as detailed in the [Managing the Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) process.</p>
</blockquote>