# Custom Apps "Configuration" tab

_Applies to: Patch My PC Cloud Custom Apps_

On the **Configuration** tab:

1. In the **Silent Install Parameters** field, enter the command-line arguments (up to a maximum of 2,048 characters) used to install the app silently (i.e. the user is not aware of the installation occurring).

> **Note**
>
> Providing \`msiexec.exe /i\` for MSI installations is not required. Using \`/qn\` will be adequate for most MSI installations.
>
> Also, see \[Supported Variables in Publisher and PMPC Cloud]\(../../../patch-my-pc-product-reference/supported-variables-in-patch-my-pc-on-premises-publisher-and-cloud.md) for a list of the variables we support in this field.

![Configuring the "Silent Install Parameters" for this app](/_images/image-(43 "Configuring the \"Silent Install Parameters\" for this app").png)

2. In the **Version** field, enter the version number for this app.

> **Note**
>
> The number entered in this field is the version of the app as shown in **Add or remove programs**.
>
> Detection uses this field to determine if the app is installed by looking for a matching **DisplayVersion** entry in the following registry key:
>
> \`HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\`

![Entering the version number for this app.](/_images/image-(42 "Entering the version number for this app.").png)

3. In the **Language** field, either type the language for this app or select it from the dropdown list.

![Configuring the language for the app](/_images/image-(41 "Configuring the language for the app").png)

4. In the **Apps & Feature Name** field, type the name of the app as it appears in **Add or remove programs**.

> **Note**
>
> Detection uses this field to determine if the app is installed by looking for a matching **DisplayName** entry in the following registry key:
>
> \`HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\`
>
> As this field allows a "**%**" wildcard (which matches on any string of characters), consider replacing the version number with this wildcard if the version number is in the **Apps & Features Name**.
>
> This will allow App Detection and Update Requirement rules to detect older versions of the app on your endpoints.

> **Important**
>
> As the **Apps & Features Name** is used to determine applicability and detection, using an overly generic name may cause Intune Updates to be detected as required on devices without the software installed.

![Entering the "Apps & Feature Name"](/_images/image-(44 "Entering the \"Apps & Feature Name\"").png)

5. Configure any additional required options from those listed below.

<table><thead><tr><th width="194.6666259765625">Field</th><th>Description</th></tr></thead><tbody><tr><td>Install Context</td><td>Controls the context in which the app is installed, either SYSTEM or <strong>User</strong>.</td></tr><tr><td>Architecture</td><td><p>Specifies the architecture for the app, either <strong>64-bit</strong> or <strong>32-bit</strong>.</p><p>Detection uses this field to determine whether to look in the 32-bit or 64-bit registry keys:</p><p><code>HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall</code></p><p>or</p><p><code>HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall</code></p></td></tr><tr><td>Conflicting processes</td><td>A comma-separated list of executables that may interfere with the installation of this app. This field populates the list for the <a href="https://patchmypc.com/manage-conflicting-processes-when-updating-third-party-applications">Manage Conflicting Processes</a> right-click feature.</td></tr><tr><td>MSI Product Code</td><td><p>Applies to MSI installers only.</p><p>The MSI Product Code for this app, which is used for detection.</p><p><mark style="color:blue;"><strong>NOTE</strong></mark></p><p>If the MSI Product Code for your installer does not update between versions, the Custom Apps Detection and Applicability rules will:</p><p>• Not detect any changes and no updates will not be installed.</p><p>• Detect the MSI app, even if an older version is installed.</p><p>To work around this issue, change the MSI Product Code to all <strong>0</strong>'s (<code>00000000-0000-0000-0000-0000</code>) when creating the Custom App. This forces the detection and applicability scripts to fall back to DisplayName and DisplayVersion detection.</p></td></tr></tbody></table>

6. If you do not want to modify the **Return Codes** for this app, go to Step 15.

> **Note**
>
> See the \[Return Codes (optional)]\(../../cloud-deployments/deploying-an-app-using-cloud/cloud-configurations-deployment-tab/return-codes-deployments.md) section of \[Deploy an App]\(../../cloud-deployments/deploying-an-app-using-cloud/) for details on managing the Return Codes for a Deployment.
>
> Also, if a Return Code defined in a Custom App has the same value but a different **Code type** to that defined in the deployment, the settings in the deployment take precedence.

7. If you do not want to add a new Return Code, proceed to Step 9.
8. To add a new Return Code for this Custom App, enter the numerical value in the **Return Code** field, select its meaning from the **Code type** dropdown, then click **Add**.

> **Note**
>
> A Return code must be a unique integer up to 10 digits long. You can add as many Return codes as your app supports. In the current release, you cannot edit or specify your own Code type as these are managed in Intune.

![Adding a new Return Code](/_images/image-(2625 "Adding a new Return Code").png)

The new Return Code is added to the list.

![New Return Code added to the list.](/_images/image-(2626 "New Return Code added to the list.").png)

9. If you do not want to edit a Return Code, go to Step 13.
10. To edit a Return Code, click the pencil icon beside it.

![Clicking the pencil icon beside a Return Code to edit it.](/_images/image-(2627 "Clicking the pencil icon beside a Return Code to edit it.").png)

11. Choose the correct **Code type** for this Return Code from the dropdown list.

![Choosing the correct "Code type" from the dropdown list](/_images/image-(2628 "Choosing the correct \"Code type\" from the dropdown list").png)

12. Click the green tick to save your changes.

![Clicking the green tick.](/_images/image-(2629 "Clicking the green tick.").png)

The **Code type** field is updated.

!["Code type" field updated.](/_images/image-(2630 "\"Code type\" field updated.").png)

13. If you do not want to delete a Return Code, go to Step 15.
14. To delete a Return Code, click the red trash can beside the relevant code.

![Deleting a Return Code](/_images/image-(2631 "Deleting a Return Code").png)

The code is deleted from the list.

![Code deleted from the list](/_images/image-(2632 "Code deleted from the list").png)

15. If you want to configure Native Detection Rules for this app, click **Next** to go to the [Detection Rules](custom-apps-detection-rules-tab.md) tab.\
    \
    If you do not want to configure Native Detection Rules, click **Next** twice to go to the [Summary ](custom-apps-summary-tab.md)tab.