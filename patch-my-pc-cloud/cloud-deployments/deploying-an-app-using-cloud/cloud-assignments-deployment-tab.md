# Cloud "Assignments" Deployment tab

_Applies to: Patch My PC Cloud_

The **Assignments** tab of the Patch My PC (PMPC) Cloud deployment wizard allows you to configure various assignments (explained below) for how you want the app to be deployed.

> \*\*Note\*\*
>
> From the \*\*Assignments\*\* page you can also:
>
> \* Apply a \[Template]\(../use-a-template-in-cloud-deployments.md) of pre-configured settings to this deployment.
>
> \* \[Enable Update Rings]\(../cloud-update-rings/create-update-rings-in-cloud.md) for this deployment.

To add an Assignment:

1. Click **Add Assignment** and then choose the assignment type you want to add for this deployment:
   1. **Add Required –** A mandatory application that will be installed automatically for all users or devices it is assigned to.
   2. **Add Available –** An optional application that will be available to install via the Company Portal for the primary user of the device.
   3. **Add Update Only –** An Intune Apps-only function that adds a mandatory update that will be installed for all users or devices it applies to. This option does not install the app or any updates to it on a device where the app has never been previously installed.

> \*\*Note\*\*
>
> If your deployment uses a \[Retention Policy]\(cloud-configurations-deployment-tab/retention-policy-deployments.md), using the \*\*Update Only\*\* assignment type will also retain the relevant number of versions of the app in addition to the regular deployment types in Intune.
>
> Also, Intune does not support using the \*\*Update Only\*\* assignment type with a deployment that is also configured to use \[ESP Profiles]\(cloud-configurations-deployment-tab/esp-profiles-deployments.md). If you try to use this configuration, the \*\*Deploy\*\* button will be greyed out and the \*\*Configurations\*\* tab will show a red "\*\*X\*\*".
>
> !\["Deploy" button greyed out and red "x" on "Configurations" tab]\(/\_images/image-(2374 "\\"Deploy\\" button greyed out and red \\"x\\" on \\"Configurations\\" tab").png>)\\
>
> \\
>
> You either need to:
>
> \* Remove the \*\*Update Only\*\* assignment type
>
> \* Or remove all ESP Profiles.

d. **Add Uninstall –** A mandatory uninstall that will remove the application from any users or devices it is assigned to, using the apps uninstaller.

> \*\*Note\*\*
>
> We do not support the \*\*Uninstall\*\* assignment type for pkg installers.
>
> See \[Uninstall a Custom App]\(../../custom-apps/custom-apps-reference/uninstall-a-custom-app.md) for more details on how the Custom Apps uninstall feature works and its limitations.

e. **Install App -** Allows the Intune admin to add **Required**, **Available**, or **Uninstall** assignments from within the Intune admin center.

f. **Update Only App -** Allows the Intune admin to add an **Update Only** assignment from within the Intune admin center.

> \*\*Note\*\*
>
> See \[Create a Deployment Without Assignments]\(../create-a-cloud-deployment-without-assignments.md) for more details on deploying apps without assignments.

![Choosing the desired assignment type](/_images/image-(2386).png)

> \*\*Note\*\*
>
> Adding an \*\*Available\*\* assignment allows you to add an \*\*Update Only\*\* application. This ensures that any applications assigned as \*\*Available\*\* are updated automatically when installed via Microsoft’s Company Portal.

2. On the **Add <**_**assignment\_type**_**> Assignment** screen, choose the relevant Entra ID security groups to target for this assignment, then click **Save**.

| Option  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Include | If checked, all of the items in this group will receive the assigned app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Exclude | <p>If checked, all of the items in this group will not receive the assigned app.<br><br>Can be used in conjunction with <strong>Include</strong> to exclude a subset of devices when you have an <strong>Include</strong> of a superset of devices.<br><br>For example, you want to target all of your computers except for your test devices. To achieve this, you'd configure your Entra ID groups as follows:<br><br>o Check <strong>Include</strong> for your <strong>All Company Devices</strong> Entra ID group.<br>o Check <strong>Exclude</strong> for your <strong>Test Devices</strong> Entra ID group.</p> |

![Choosing the relevant Entra ID security groups to target for this assignment](/_images/image-(2387).png)

> \*\*Note\*\*
>
> As our portal uses application permissions to read Entra ID groups, all groups will be visible whenever you manage assignments.

The **Assignments** page updates to show the newly added assignments, including their configuration.

!["Assignments" page updates to show the newly added assignments](/_images/image-(2388).png)

3. Make any of the following optional modifications to the assignment(s).

| Option           | Description                                                                                                                                               |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add Filter       | The ability to add filters you have already created in Intune to target specific device types for the deployment.                                         |
| Notifications    | When to display notifications related to this deployment.                                                                                                 |
| Content Download | <p>How to download the content for the deployment:<br><br>o Foreground - The default for initial installs.<br>o Background - The default for updates.</p> |

> \*\*Note\*\*
>
> We automatically configure these settings based on our experience and best practices, but you can modify certain settings if necessary.

> \*\*Tip\*\*
>
> You can click \*\*Deploy\*\* on this page if you don’t want to add additional assignments or see the \*\*Summary\*\* page, which allows you to double-check the settings you’ve configured for this deployment.

4. Add any additional assignments for this deployment by clicking **Add Assignment** and repeating the steps in this section.
5.  If you are happy you have entered all of the details for the deployment correctly, click **Deploy** to deploy the app. However, we recommend you click **Next** to move to the [**Summary** ](cloud-summary-deployment-tab.md)tab, where you can verify the settings for this deployment before you deploy this app.\\

    ![Clicking "Deploy" to deploy the app](/_images/image-(2390).png)