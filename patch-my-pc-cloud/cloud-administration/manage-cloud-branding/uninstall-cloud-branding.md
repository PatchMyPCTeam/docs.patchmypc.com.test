# Uninstall Cloud Branding

_Applies to: Patch My PC Cloud_

To uninstall any custom logos or localizations from your end-user devices installed by a Patch My PC (PMPC ) Cloud Branding App, you need to uninstall the relevant Branding App.

Simply [deleting a Branding App](delete-cloud-branding.md) only removes that Branding App from Intune.

Creating an **Uninstall Branding App** creates a Win32 app in Intune with a **Required** assignment with an uninstall intent, that will remove any PMPC Cloud custom branding files from the assigned devices.

{% hint style="danger" %}
**Important**

Each device can only have one Branding App installed. Even if you have multiple branding apps assigned to the same device, only the one that was installed last will be installed on the device.

The script that the Uninstall Branding App runs removes the branding currently installed on the device. It does not check which specific branding was originally deployed.

For example, if you assign the uninstall for Branding A, but the device now has Branding B, Branding B will be removed.

This is why when you create an Uninstall Branding App, a new Win32 app is created that will uninstall any Branding App the targeted device may have installed.
{% endhint %}

To uninstall a Branding app:

1. Navigate to **Settings | Branding**

![Navigating to “Settings | Branding”](../../../_images/image%20%282650%29.png%20"Navigating%20to%20\"Settings%20|%20Branding\"")

2.  On the **Branding** screen, make a note of the assignments for the branding app you want to uninstall.\


    For example, if you plan to uninstall the **Branding – Corel Users** branding app, make a note of which resources it is assigned to by hovering over **Assignments** and noting the assignments (**Corel All Users** in this example).

![Making a note of the assignments for the Branding App to be uninstalled.](../../../_images/image%20%282651%29.png%20"Making%20a%20note%20of%20the%20assignments%20for%20the%20Branding%20App%20to%20be%20uninstalled.")

3.  Follow [Delete Cloud Branding V2](delete-cloud-branding.md) to delete the Branding App that is to be uninstalled.\


    This not only deletes the Branding App from Intune, but also avoids a potential loop of the branding being installed by the Branding App and then uninstalled by the Branding Uninstall App.
4. On the **Branding** screen, click **Uninstall Brandings**

![Clicking “Uninstall Brandings”](../../../_images/image%20%282652%29.png%20"Clicking%20\"Uninstall%20Brandings\"")

5. In the **Uninstall Branding App Name** field, type a unique name for the Intune Win32 app that will be used to uninstall the Branding App.

![Entering a unique name in the “Uninstall Branding App Name” field](../../../_images/image%20%282653%29.png%20"Entering%20a%20unique%20name%20in%20the%20\"Uninstall%20Branding%20App%20Name\"%20field")

6. Click **Add Assignment**

![Clicking “Add Assignment](../../../_images/image%20%282654%29.png%20"Clicking%20\"Add%20Assignment")

7. On the **Add Uninstall Assignment** page, select the relevant resources noted in step 2 that this uninstall should be targeted to and click **Save**.

![Select the relevant resources this uninstall should be targeted at and clicking “Save”](../../../_images/image%20%282655%29.png%20"Select%20the%20relevant%20resources%20this%20uninstall%20should%20be%20targeted%20at%20and%20clicking%20\"Save\"")

The list of assignments is updated to show that the **Uninstall** assignment has been added for the selected resources.

{% hint style="danger" %}
**Important**

Assigning the Uninstall Branding App to a resource will remove all PMPC Cloud-related brandings and associated files and localizations.&#x20;
{% endhint %}

![List of assignments updated to show the “Uninstall” assignment has been added for the selected resources.](../../../_images/image%20%2817%29.png%20"List%20of%20assignments%20updated%20to%20show%20the%20\"Uninstall\"%20assignment%20has%20been%20added%20for%20the%20selected%20resources.")

8. If the list of assignments is correct, proceed to step 9; otherwise, repeat steps 6 and 7 to add any additional assignments.

{% hint style="success" %}
**Tip**

You can delete an assignment by clicking the trash can beside it.
{% endhint %}

9. Click **Save** to continue.

![Clicking “Save” to continue](../../../_images/image%20%282657%29.png%20"Clicking%20\"Save\"%20to%20continue")

The **Branding** page is redisplayed, showing the new **Uninstall App** at the top, along with the **Success – Uninstall Branding app created** notification.

{% hint style="success" %}
**Tip**

You can tell which Branding App is the uninstall as it has **UNINSTALL BRANDING** for it's company logo.
{% endhint %}

![“Branding” page redisplayed showing the new uninstall app along with the “Success – Branding created” notification.](../../../_images/image%20%2818%29.png%20"\"Branding\"%20page%20redisplayed%20showing%20the%20new%20uninstall%20app%20along%20with%20the%20\"Success%20–%20Branding%20created\"%20notification.")

{% hint style="info" %}
**Note**

You can only create one Branding Uninstall App, which, like other apps, can be edited, recreated, and deleted. If you need to uninstall branding from different resources, you will need to:

1. Edit the existing Branding Uninstall App by clicking on the ellipsis (**⋮**) beside it and selecting **Edit**.
2. Changing the name of the Uninstall Branding app as required.
3. Amend the assignments to the corresponding resources you wish to remove branding from.
4. Save your changes.

Also, when deploying a new Branding App, if you already have an Uninstall App, check to ensure the Uninstall App is not assigned to the same resources as the Branding App, otherwise, you could encounter an unwanted loop with the Branding App being installed, but then uninstalled by the Uninstall Branding App.
{% endhint %}
