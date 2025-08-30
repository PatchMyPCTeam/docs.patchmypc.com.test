# Update a Cloud Update Ring

_Applies to: Patch My PC Cloud_

If you are using the Update Rings feature of Patch My PC (PMPC) Cloud, you may find that a version of an app deployed to a ring works fine and you now want to deploy this version to the next update ring without waiting for either the configured delay to be reached for that ring or the [Sync Schedule](../../cloud-administration/manage-the-sync-schedule-in-cloud.md) to be run.

To update an individual Update Ring to a later version:

1. Navigate to the **Deployments** node.
2.  Click the relevant deployment to open its properties then click **More Info**.\


    ![Clicking “More Info”](../../../_images/image%20%282143%29.png%20"Clicking%20\"More%20Info\"")


3.  If you can update a ring to a newer version the **Update Now** button is available.\


    ![“Update Now” button available](../../../_images/image%20%282144%29.png%20"\"Update%20Now\"%20button%20available")



{% hint style="warning" %}
**Important**

Some important points to note:

* The **Update Now** option is only available if the deployment has been deployed successfully. It will not be shown if the deployment is in any other state or if **Pause Updates** has been enabled for this deployment.
* An individual update ring can only be updated to a later version than the one it is currently running.
* An individual update ring can only be updated to a later version that has already been applied to the ring with the lowest delay.
* You are only updating a specific ring to a later version, not the whole deployment or any other rings.
{% endhint %}

4.  Click **Update Now** and select the relevant version you want to upgrade this ring to.\


    ![Selecting which version to update this ring to](../../../_images/image%20%282145%29.png%20"Selecting%20which%20version%20to%20update%20this%20ring%20to")


5.  On the **Update “<**_**deployment\_name**_**>” ring to version <**_**version\_number**_**>** dialog box, click **Confirm**.\


    ![Clicking “Confirm”](../../../_images/image%20%282147%29.png%20"Clicking%20\"Confirm\"")

    \
    The portal refreshes showing that the deployment is **In Progress** and the **Success – Ring <**_**ring\_name**_**>** updated notification is shown.\


    ![](../../../_images/image%20%282148%29.png%20"")

    \
    Once the deployment has completed successfully, if you navigate back to the ring, you will see the version number has changed and the **Update Now** button is unavailable.\


    ![Version number has changed and “Update Now” button is unavailable.](../../../_images/image%20%282149%29.png%20"Version%20number%20has%20changed%20and%20\"Update%20Now\"%20button%20is%20unavailable.")
