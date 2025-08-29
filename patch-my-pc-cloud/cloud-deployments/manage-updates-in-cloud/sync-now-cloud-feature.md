# "Sync Now" Cloud feature

_Applies to: Patch My PC Cloud_

{% hint style="info" %}
**Note**

If an app has more than one version of an update available, using **Sync Now** ensures it is updated to the latest version as soon as possible, which could impact your users. So, think carefully before using this.
{% endhint %}

If you have [resumed updates](resume-cloud-updates.md) for an app in Patch My PC (PMPC) Cloud and want to update it as soon as possible rather than waiting for the nightly sync job to run:

1.  Click on the relevant deployment which has been resumed.\


    ![Clicking on the relevant successful deployment for which updates have been resumed](../../../_images/image%20%282004%29.png%20"Clicking%20on%20the%20relevant%20successful%20deployment%20for%20which%20updates%20have%20been%20resumed")
2.  Click **Sync Now** to install any updates for the app immediately.\
    \


    ![Clicking “Sync Now”](../../../_images/image%20%282005%29.png%20"Clicking%20\"Sync%20Now\"")

{% hint style="info" %}
**Note**

If the **Sync Now** button is greyed out, no updates are available for this app.
{% endhint %}

3.  On the **Are you sure you want to update <**_**app\_name**_**> to the latest version** popup, click **OK**.\


    ![](../../../_images/image%20%281828%29.png%20"")

    \
    The **Deployment <**_**app\_name**_**> updated** notification is displayed and the deployment **Status** changes to **In Progress**.\


    ![](../../../_images/image%20%281829%29.png%20"")

    \
    Once the deployment has been completed successfully, the **Status** changes to **Success**.\


    ![“Status” changing to Success.](../../../_images/image%20%281830%29.png%20"\"Status\"%20changing%20to%20Success.")

{% hint style="success" %}
**Tip**

If you look in the **Events node**, you will see the following event:

**Deployment <**_**app\_name**_**> Updated.**
{% endhint %}
