# Resume Cloud Updates

_Applies to: Patch My PC Cloud_

If the _Pause Updates_ feature of Patch My PC (PMPC) Cloud has been configured for an app that has since been updated, and you want to bring the app up-to-date to the latest version, you need to disable pause updates.

{% hint style="info" %}
**Note**

If an app has more than one version of an update available, resuming updates will ensure it is updated to the latest version.

Also, if you paused a deployment with [Update Rings](../cloud-update-rings/) enabled, when you resume updates for that deployment, the Update Rings are re-enabled and function normally.
{% endhint %}

To resume updates for an app:

1. Click on the relevant deployment that has been paused.

{% hint style="success" %}
**Tip**

Click the filter button (![](../../../_images/image%20%282513).png>)) and select the **Enabled** option under the **Updates** section, followed by **Apply Filters** to see just those deployments that have updates paused.&#x20;
{% endhint %}

![Clicking on the relevant successful deployment which has been paused for updates](../../../_images/image%20%282000%29.png%20"Clicking%20on%20the%20relevant%20successful%20deployment%20which%20has%20been%20paused%20for%20updates")

2.  Click the **Pause Updates** slider to disable it.\


    ![Clicking the “Pause Updates” slider](../../../_images/image%20%282001%29.png%20"Clicking%20the%20\"Pause%20Updates\"%20slider")

{% hint style="info" %}
**Note**

Notice on the above screenshot that the **Sync Now** button is available, meaning one or more updates are available for this app.
{% endhint %}

3.  Click the **X** to close the deployment properties page.\


    ![Clicking “X” to close the deployment properties page](../../../_images/image%20%282002%29.png%20"Clicking%20\"X\"%20to%20close%20the%20deployment%20properties%20page")

    \
    The list of deployments is displayed without **UPDATES PAUSED** under the deployment you just unpaused.\


    ![&#x22;UPDATES PAUSED&#x22; no longer under the deployment name.](../../../_images/image%20%282003%29.png%20"&#x22;UPDATES%20PAUSED&#x22;%20no%20longer%20under%20the%20deployment%20name.")

Updates for this app are now resumed.

You now need to decide how you want to install any updates for this app:

* **Install the updates now –** If you want to install the updates as soon as possible, follow the [Sync Now](sync-now-cloud-feature.md) process.
* **Wait for the nightly sync to run –** If you are happy to wait for the updates to be installed the next time the daily sync runs (at 2 am by default), you do not need to do anything.

{% hint style="info" %}
**Note**

You can change the Sync Schedule to a different time, as detailed in the [Managing the Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) process.
{% endhint %}
