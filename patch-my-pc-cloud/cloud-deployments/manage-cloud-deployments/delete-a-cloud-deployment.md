# Delete a Cloud Deployment

_Applies to: Patch My PC Cloud_

To delete a deployment in Patch My PC (PMPC) Cloud:

1.  From the <strong>Deployments</strong> page, click the ellipsis (<strong>⋮</strong>) beside the relevant deployment you want to delete and click <strong>Delete</strong>.\


    ![Clicking the ellipsis beside a deployment and selecting “Delete”](/_images/image-(1684).png "Clicking the ellipsis beside a deployment and selecting “Delete”")


2.  On the <strong>Are you sure you want to delete <</strong>_<strong>deployment\_name</strong>_<strong>></strong> dialog box, click <strong>Yes</strong>.\


    ![](/_images/image-(869).png "")



<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If the deployment you are deleting is for an app that another app is dependent on, the <strong>Are you sure</strong> dialog box will state which app has a dependency on this deployment and warn you that proceeding will delete this dependency, which could break the app dependent on this one.</p>
<p>![“Are you sure” prompt if other deployments have dependencies on this one](/_images/image (2276).png>)</p>
</blockquote>

The deployment is deleted and the <strong>Success - Deployment&#x20;</strong>_<strong>\<deployment\_name></strong>_<strong>&#x20;deleted</strong> notification is displayed.

<blockquote class="wp-block-quote">
<p><strong>Warning</strong></p>
<p>Deleting a deployment will also delete the:</p>
<p>* latest and all old unassigned versions of this deployment if a [Retention Policy](../deploying-an-app-using-cloud/cloud-configurations-deployment-tab/retention-policy-deployments.md) has been configured.</p>
<p>* packaged win32 app from Intune.</p>
</blockquote>

![](/_images/image-(1685).png "")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can also click <strong>Delete</strong> on the property page of a deployment to delete it.</p>
</blockquote>