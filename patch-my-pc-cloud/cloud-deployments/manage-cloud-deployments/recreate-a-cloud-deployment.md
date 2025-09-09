# Recreate a Cloud Deployment

_Applies to: Patch My PC Cloud_

Using Patch My PC (PMPC) Cloud, you can delete software from Intune and recreate it to retrigger the deployment on the targeted resources.

To recreate a deployment:

1.  From the <strong>Deployments</strong> page, click the ellipsis (<strong>⋮</strong>) beside the relevant deployment you want to recreate and click <strong>Recreate</strong>.\


    ![Clicking the ellipsis beside a deployment and selecting “Recreate”](/_images/image-(2013).png "Clicking the ellipsis beside a deployment and selecting “Recreate”")
2.  On the <strong>Are you sure you want to recreate <</strong>_<strong>deployment\_name</strong>_<strong>></strong> dialog box, click <strong>Yes</strong>.\


    ![](/_images/image-(1681).png "")

    \
    The <strong>Status</strong> of the deployment changes to <strong>In Progress</strong> and the <strong>Recreating the deployment&#x20;</strong>_<strong>\<deployment\_name></strong>_<strong>&#x20;has started</strong> message is displayed.\


    ![Change to deployment status and message stating the recreation process has started](/_images/image-(1682).png "Change to deployment status and message stating the recreation process has started")

    \
    Once the deployment has been recreated, the portal auto-refreshes and the <strong>Status</strong> changes to <strong>Success</strong>.\


    ![Portal auto-refreshes to show the deployment has been successfully recreated](/_images/image-(1683).png "Portal auto-refreshes to show the deployment has been successfully recreated")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>You can also click <strong>Recreate</strong> on the property page of a deployment to recreate it.</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If the deployment you are recreating has [Update Rings](../cloud-update-rings/) enabled, clicking <strong>Recreate</strong> will result in duplicate versions of the apps being created in Intune. Any existing assignments will be automatically moved from the old version to the new, recreated version.</p>
<p>Also, if the deployment you are recreating has [App Dependencies](../deploying-an-app-using-cloud/cloud-configurations-deployment-tab/dependencies-deployments.md), clicking <strong>Recreate</strong> creates a new app, creates any dependencies, deletes the dependencies for the old app, and finally deletes the old app from Intune.</p>
</blockquote>