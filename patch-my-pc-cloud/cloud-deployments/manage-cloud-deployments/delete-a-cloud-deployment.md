# Delete a Cloud Deployment

_Applies to: Patch My PC Cloud_

To delete a deployment in Patch My PC (PMPC) Cloud:

1.  From the **Deployments** page, click the ellipsis (**⋮**) beside the relevant deployment you want to delete and click **Delete**.\


    ![Clicking the ellipsis beside a deployment and selecting “Delete”](/_images/image-(1684).png "Clicking the ellipsis beside a deployment and selecting “Delete”")


2.  On the **Are you sure you want to delete <**_**deployment\_name**_**>** dialog box, click **Yes**.\


    ![](/_images/image-(869).png "")



{% hint style="info" %}
**Note**

If the deployment you are deleting is for an app that another app is dependent on, the **Are you sure** dialog box will state which app has a dependency on this deployment and warn you that proceeding will delete this dependency, which could break the app dependent on this one.

![“Are you sure” prompt if other deployments have dependencies on this one](/_images/image-(2276 "“Are you sure” prompt if other deployments have dependencies on this one").png>)
{% endhint %}

The deployment is deleted and the **Success - Deployment&#x20;**_**\<deployment\_name>**_**&#x20;deleted** notification is displayed.

{% hint style="danger" %}
**Warning**

Deleting a deployment will also delete the:

* latest and all old unassigned versions of this deployment if a [Retention Policy](../deploying-an-app-using-cloud/cloud-configurations-deployment-tab/retention-policy-deployments.md) has been configured.
* packaged win32 app from Intune.
{% endhint %}

![](/_images/image-(1685).png "")

{% hint style="success" %}
**Tip**

You can also click **Delete** on the property page of a deployment to delete it.
{% endhint %}
