# Create a Cloud Deployment Without Assignments

_Applies to: Patch My PC Cloud_

Some large organizations want to be able to create deployments in Intune Apps for Patch My PC (PMPC) Cloud without any assignments.

Then, their local IT organization adds and manages the assignments to the relevant deployments to meet their needs by using Intune admin center.

To create a deployment with no assignments:

1.  Follow the [Deploy an App](deploying-an-app-using-cloud/) process until you reach the[ Assignments](deploying-an-app-using-cloud/cloud-assignments-deployment-tab.md) tab where you can add an assignment.\
    \
    When you click **Add Assignment**, you will see the **App Without Assignment** sub-menu containing the following two items:\
    \
    \&#xNAN;**• Install App -** Allows the Intune admin to add **Required**, **Available**, or **Uninstall** assignments from within the Intune admin center.\
    \
    • **Update Only App -** Allows the Intune admin to add only an **Update Only** assignment from within the Intune admin center.\\

    !["App Without Assignment" sub-menu](/_images/image-(358 "\"App Without Assignment\" sub-menu").png)

> **Note**
>
> If you are deploying a Microsoft patch file (**.msp**), only the **Update Only App** option is shown under the **App Without Assignment** section as **.msp** files cannot be used to install an app, only update it.

> **Tip**
>
> You can also \[Add a Template]\(../cloud-administration/manage-cloud-deployment-templates/add-a-cloud-deployment-template.md) with the **App Without Assignments** options configured. Then when you create the deployment, simply click **Apply Template** and select the relevant template to have its settings applied to this deployment.

2.  Select the relevant option.\\

    ![Selecting the required option](/_images/image-(2483 "Selecting the required option").png)
3.  Uncheck the **Copy-Forward** checkbox if required.\
    \
    This checkbox is checked by default, which means whenever we see any manually created assignments on Intune, when we update the app, we’ll automatically copy forward all the assignments from the previous version to the new version.\\

    !["Copy-Forward" checkbox](/_images/image-(2484 "\"Copy-Forward\" checkbox").png)
4.  Click **Deploy** and wait for the deployment to complete successfully.\\

    ![Clicking "Deploy"](/_images/image-(2485 "Clicking \"Deploy\"").png)

Once the deployment has successfully completed, if you look in the Intune admin center you will see that the app has been created without any assignments.

![App created with no assignments](/_images/image-(362 "App created with no assignments").png)

Your local IT teams can now follow the [Assign apps to groups with Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/apps/apps-deploy) process to add the relevant assignments for this app.

> **Note**
>
> If you checked the **Copy-Forward** checkbox, the next time the Sync Schedule detects a new version, the assignments are copied forward to the new version. The old version of the app will be removed immediately once the new version has been created and the assignments moved over to it.
>
> Also, a deployment without assignments can be edited and managed in the same way as a regular deployment. See the \[Manage Updates]\(manage-updates-in-cloud/) and \[Manage Deployments]\(manage-cloud-deployments/) sections for more details.

> **Important**
>
> The current release of this feature has the following restrictions:
>
> \* A deployment cannot contain both regular assignment types and no assignment types.
>
> \* If you edit a deployment with no assignments, you cannot add a regular assignment type.
>
> \* If you have a regular deployment with update rings enabled, you cannot edit that deployment, disable update rings, remove all the assignments and then add a new no assignment type.