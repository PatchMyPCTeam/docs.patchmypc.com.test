# Update a Cloud Update Ring

_Applies to: Patch My PC Cloud_

If you are using the Update Rings feature of Patch My PC (PMPC) Cloud, you may find that a version of an app deployed to a ring works fine and you now want to deploy this version to the next update ring without waiting for either the configured delay to be reached for that ring or the [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) to be run.

To update an individual Update Ring to a later version:

1. Navigate to the **Deployments** node.
2.  Click the relevant deployment to open its properties then click **More Info**.\


    <figure><img src="../../../_images/gitbook/image%20%282143%29.png" alt="Clicking “More Info”"><figcaption></figcaption></figure>


3.  If you can update a ring to a newer version the **Update Now** button is available.\


    <figure><img src="../../../_images/gitbook/image%20%282144%29.png" alt="“Update Now” button available"><figcaption></figcaption></figure>



{% hint style="warning" %}
**Important**

Some important points to note:

* The **Update Now** option is only available if the deployment has been deployed successfully. It will not be shown if the deployment is in any other state or if **Pause Updates** has been enabled for this deployment.
* An individual update ring can only be updated to a later version than the one it is currently running.
* An individual update ring can only be updated to a later version that has already been applied to the ring with the lowest delay.
* You are only updating a specific ring to a later version, not the whole deployment or any other rings.
{% endhint %}

4.  Click **Update Now** and select the relevant version you want to upgrade this ring to.\


    <figure><img src="../../../_images/gitbook/image%20%282145%29.png" alt="Selecting which version to update this ring to"><figcaption></figcaption></figure>


5.  On the **Update “<**_**deployment\_name**_**>” ring to version <**_**version\_number**_**>** dialog box, click **Confirm**.\


    <figure><img src="../../../_images/gitbook/image%20%282147%29.png" alt="Clicking “Confirm”" width="455"><figcaption></figcaption></figure>

    \
    The portal refreshes showing that the deployment is **In Progress** and the **Success – Ring <**_**ring\_name**_**>** updated notification is shown.\


    <figure><img src="../../../_images/gitbook/image%20%282148%29.png" alt="Deployment shows as “In Progress” and the “Success – Ring <ring_name> updated” notification is shown."><figcaption></figcaption></figure>

    \
    Once the deployment has completed successfully, if you navigate back to the ring, you will see the version number has changed and the **Update Now** button is unavailable.\


    <figure><img src="../../../_images/gitbook/image%20%282149%29.png" alt="Version number has changed and “Update Now” button is unavailable."><figcaption></figcaption></figure>
