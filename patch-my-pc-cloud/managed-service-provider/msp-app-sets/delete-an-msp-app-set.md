# Delete an MSP App Set

_Applies to: Patch My PC Cloud_

To delete an MSP App Set:

{% hint style="info" %}
**Note**

This process covers deleting an entire App Set. If you want to delete just a specific application or assignment from an App Set, you should follow the [Edit an App Set](edit-an-msp-app-set.md) process.

You cannot delete an App Set with a **Status** of **In progress** and once the deletion of the App Set has begun, you will be unable to perform any other actions on it.
{% endhint %}

1.  Navigate to **App Sets**\


    ![Navigating to “App Sets”](../../../_images/image%20%282559%29.png%20"Navigating%20to%20\"App%20Sets\"")
2.  Click the ellipsis (**⋮**) beside the App Set you want to delete and select **Delete**\
    \


    ![Clicking the ellipsis beside the App Set you want to delete and selecting “Delete”](../../../_images/image%20%282560%29.png%20"Clicking%20the%20ellipsis%20beside%20the%20App%20Set%20you%20want%20to%20delete%20and%20selecting%20\"Delete\"")
3.  On the **Are you sure you want to delete <**_**app\_set\_name>**_ dialog box, click **Yes**\


    ![Clicking “Yes” on the “Are you sure you want to delete” dialog box](../../../_images/image%20%282561%29.png%20"Clicking%20\"Yes\"%20on%20the%20\"Are%20you%20sure%20you%20want%20to%20delete\"%20dialog%20box")

    \
    The **Success – Deletion the App Set <**_**appset\_name**_**> has started** notification is shown and the App Set has a **Status** of **Deleting** whilst the App Set and it’s associated deployments are removed from the relevant companies.\


    ![Notification the App Set is being deleted](../../../_images/image%20%282562%29.png%20"Notification%20the%20App%20Set%20is%20being%20deleted")

{% hint style="info" %}
**Note**

Deleting an App Set automatically deletes all of the deployments for all of the apps from all of the companies to which it was deployed. You don’t need to delete the individual deployments from the targeted companies before deleting the App Set.
{% endhint %}

Once the App Set has been successfully deleted (which can take an extended period of time depending on its contents and where it’s been deployed), the App Set will disappear from the **App Set** page.

![“App Set” page showing the App Set has been deleted](../../../_images/image%20%282563%29.png%20"\"App%20Set\"%20page%20showing%20the%20App%20Set%20has%20been%20deleted")
