# Recreate a Cloud Deployment

_Applies to: Patch My PC Cloud_

Using Patch My PC (PMPC) Cloud, you can delete software from Intune and recreate it to retrigger the deployment on the targeted resources.

To recreate a deployment:

1.  From the **Deployments** page, click the ellipsis (**⋮**) beside the relevant deployment you want to recreate and click **Recreate**.\


    ![Clicking the ellipsis beside a deployment and selecting “Recreate”](../../../_images/image%20%282013%29.png%20"Clicking%20the%20ellipsis%20beside%20a%20deployment%20and%20selecting%20\"Recreate\"")
2.  On the **Are you sure you want to recreate <**_**deployment\_name**_**>** dialog box, click **Yes**.\


    ![](../../../_images/image%20%281681%29.png%20"")

    \
    The **Status** of the deployment changes to **In Progress** and the **Recreating the deployment&#x20;**_**\<deployment\_name>**_**&#x20;has started** message is displayed.\


    ![Change to deployment status and message stating the recreation process has started](../../../_images/image%20%281682%29.png%20"Change%20to%20deployment%20status%20and%20message%20stating%20the%20recreation%20process%20has%20started")

    \
    Once the deployment has been recreated, the portal auto-refreshes and the **Status** changes to **Success**.\


    ![Portal auto-refreshes to show the deployment has been successfully recreated](../../../_images/image%20%281683%29.png%20"Portal%20auto-refreshes%20to%20show%20the%20deployment%20has%20been%20successfully%20recreated")

{% hint style="success" %}
**Tip**

You can also click **Recreate** on the property page of a deployment to recreate it.
{% endhint %}

{% hint style="info" %}
**Note**

If the deployment you are recreating has [Update Rings](../cloud-update-rings/) enabled, clicking **Recreate** will result in duplicate versions of the apps being created in Intune. Any existing assignments will be automatically moved from the old version to the new, recreated version.

Also, if the deployment you are recreating has [App Dependencies](../deploying-an-app-using-cloud/cloud-configurations-deployment-tab/dependencies-deployments.md), clicking **Recreate** creates a new app, creates any dependencies, deletes the dependencies for the old app, and finally deletes the old app from Intune.
{% endhint %}
