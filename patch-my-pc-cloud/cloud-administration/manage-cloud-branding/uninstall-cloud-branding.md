# Uninstall Cloud Branding

_Applies to: Patch My PC Cloud_

To uninstall any custom logos or localizations from your end-user devices installed by a Patch My PC (PMPC ) Cloud Branding App, you need to uninstall the relevant Branding App.

Simply [deleting a Branding App](delete-cloud-branding.md) only removes that Branding App from Intune.

Creating an **Uninstall Branding App** creates a Win32 app in Intune with a **Required** assignment with an uninstall intent, that will remove any PMPC Cloud custom branding files from the assigned devices.

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>Each device can only have one Branding App installed. Even if you have multiple branding apps assigned to the same device, only the one that was installed last will be installed on the device.</p>
<p>The script that the Uninstall Branding App runs removes the branding currently installed on the device. It does not check which specific branding was originally deployed.</p>
<p>For example, if you assign the uninstall for Branding A, but the device now has Branding B, Branding B will be removed.</p>
<p>This is why when you create an Uninstall Branding App, a new Win32 app is created that will uninstall any Branding App the targeted device may have installed.</p>
</blockquote>

To uninstall a Branding app:

1. Navigate to **Settings | Branding**

![Navigating to "Settings | Branding"](/_images/image-(2650Settings-Branding "Navigating to \"Settings | Branding\"").png "Navigating to “Settings | Branding”")

2.  On the **Branding** screen, make a note of the assignments for the branding app you want to uninstall.\


    For example, if you plan to uninstall the **Branding – Corel Users** branding app, make a note of which resources it is assigned to by hovering over **Assignments** and noting the assignments (**Corel All Users** in this example).

![Making a note of the assignments for the Branding App to be uninstalled.](/_images/image-(2651 "Making a note of the assignments for the Branding App to be uninstalled.").png "Making a note of the assignments for the Branding App to be uninstalled.")

3.  Follow [Delete Cloud Branding V2](delete-cloud-branding.md) to delete the Branding App that is to be uninstalled.\


    This not only deletes the Branding App from Intune, but also avoids a potential loop of the branding being installed by the Branding App and then uninstalled by the Branding Uninstall App.
4. On the **Branding** screen, click **Uninstall Brandings**

![Clicking "Uninstall Brandings"](/_images/image-(2652Uninstall-Brandings "Clicking \"Uninstall Brandings\"").png "Clicking “Uninstall Brandings”")

5. In the **Uninstall Branding App Name** field, type a unique name for the Intune Win32 app that will be used to uninstall the Branding App.

![Entering a unique name in the "Uninstall Branding App Name" field](/_images/image-(2653Uninstall-Branding-App-Name "Entering a unique name in the \"Uninstall Branding App Name\" field").png "Entering a unique name in the “Uninstall Branding App Name” field")

6. Click **Add Assignment**

![Clicking "Add Assignment](/_images/image-(2654Add-Assignment "Clicking \"Add Assignment").png "Clicking “Add Assignment")

7. On the **Add Uninstall Assignment** page, select the relevant resources noted in step 2 that this uninstall should be targeted to and click **Save**.

![Select the relevant resources this uninstall should be targeted at and clicking "Save"](/_images/image-(2655Save "Select the relevant resources this uninstall should be targeted at and clicking \"Save\"").png "Select the relevant resources this uninstall should be targeted at and clicking “Save”")

The list of assignments is updated to show that the **Uninstall** assignment has been added for the selected resources.

<blockquote class="wp-block-quote">
<p>**Important**</p>
<p>Assigning the Uninstall Branding App to a resource will remove all PMPC Cloud-related brandings and associated files and localizations.&#x20;</p>
</blockquote>

![List of assignments updated to show the "Uninstall" assignment has been added for the selected resources.](/_images/image-(17Uninstall." "List of assignments updated to show the \"Uninstall\" assignment has been added for the selected resources.").png "List of assignments updated to show the “Uninstall” assignment has been added for the selected resources.")

8. If the list of assignments is correct, proceed to step 9; otherwise, repeat steps 6 and 7 to add any additional assignments.

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can delete an assignment by clicking the trash can beside it.</p>
</blockquote>

9. Click **Save** to continue.

![Clicking "Save" to continue](/_images/image-(2657Save "Clicking \"Save\" to continue").png "Clicking “Save” to continue")

The **Branding** page is redisplayed, showing the new **Uninstall App** at the top, along with the **Success – Uninstall Branding app created** notification.

<blockquote class="wp-block-quote">
<p>**Tip**</p>
<p>You can tell which Branding App is the uninstall as it has **UNINSTALL BRANDING** for it's company logo.</p>
</blockquote>

!["Branding" page redisplayed showing the new uninstall app along with the "Success – Branding created" notification.](/_images/image-(18Branding." "\"Branding\" page redisplayed showing the new uninstall app along with the \"Success – Branding created\" notification.").png "“Branding” page redisplayed showing the new uninstall app along with the “Success – Branding created” notification.")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>You can only create one Branding Uninstall App, which, like other apps, can be edited, recreated, and deleted. If you need to uninstall branding from different resources, you will need to:</p>
<p>1. Edit the existing Branding Uninstall App by clicking on the ellipsis (**⋮**) beside it and selecting **Edit**.</p>
<p>2. Changing the name of the Uninstall Branding app as required.</p>
<p>3. Amend the assignments to the corresponding resources you wish to remove branding from.</p>
<p>4. Save your changes.</p>
<p>Also, when deploying a new Branding App, if you already have an Uninstall App, check to ensure the Uninstall App is not assigned to the same resources as the Branding App, otherwise, you could encounter an unwanted loop with the Branding App being installed, but then uninstalled by the Uninstall Branding App.</p>
</blockquote>