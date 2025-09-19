# Recreate a Cloud Deployment

_Applies to: Patch My PC Cloud_

Using Patch My PC (PMPC) Cloud, you can delete software from Intune and recreate it to retrigger the deployment on the targeted resources.

To recreate a deployment:

1.  From the **Deployments** page, click the ellipsis (**⋮**) beside the relevant deployment you want to recreate and click **Recreate**.\\

    ![Clicking the ellipsis beside a deployment and selecting “Recreate”](../../../.gitbook/assets/image-\(2013\).png)
2.  On the **Are you sure you want to recreate <**_**deployment\_name**_**>** dialog box, click **Yes**.\\

    ![](../../../.gitbook/assets/image-\(1681\).png)

    \
    The **Status** of the deployment changes to **In Progress** and the **Recreating the deployment&#x20;**_**\<deployment\_name>**_**&#x20;has started** message is displayed.\\

    ![Change to deployment status and message stating the recreation process has started](../../../.gitbook/assets/image-\(1682\).png)

    \
    Once the deployment has been recreated, the portal auto-refreshes and the **Status** changes to **Success**.\\

    ![Portal auto-refreshes to show the deployment has been successfully recreated](../../../.gitbook/assets/image-\(1683\).png)

> **Tip**
>
> You can also click **Recreate** on the property page of a deployment to recreate it.

> **Note**
>
> If the deployment you are recreating has \[Update Rings]\(../cloud-update-rings/) enabled, clicking **Recreate** will result in duplicate versions of the apps being created in Intune. Any existing assignments will be automatically moved from the old version to the new, recreated version.
>
> Also, if the deployment you are recreating has \[App Dependencies]\(../deploying-an-app-using-cloud/cloud-configurations-deployment-tab/dependencies-deployments.md), clicking **Recreate** creates a new app, creates any dependencies, deletes the dependencies for the old app, and finally deletes the old app from Intune.
