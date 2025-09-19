# Delete an MSP App Set

_Applies to: Patch My PC Cloud_

To delete an MSP App Set:

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>This process covers deleting an entire App Set. If you want to delete just a specific application or assignment from an App Set, you should follow the [Edit an App Set](edit-an-msp-app-set.md) process.</p>
<p>You cannot delete an App Set with a **Status** of **In progress** and once the deletion of the App Set has begun, you will be unable to perform any other actions on it.</p>
</blockquote>

1.  Navigate to **App Sets**\


    ![Navigating to "App Sets"](/_images/image-(2559 "Navigating to \"App Sets\"").png "Navigating to “App Sets”")
2.  Click the ellipsis (**⋮**) beside the App Set you want to delete and select **Delete**\
    \


    ![Clicking the ellipsis beside the App Set you want to delete and selecting "Delete"](/_images/image-(2560 "Clicking the ellipsis beside the App Set you want to delete and selecting \"Delete\"").png "Clicking the ellipsis beside the App Set you want to delete and selecting “Delete”")
3.  On the **Are you sure you want to delete <**_**app\_set\_name>**_ dialog box, click **Yes**\


    ![Clicking "Yes" on the "Are you sure you want to delete" dialog box](/_images/image-(2561 "Clicking \"Yes\" on the \"Are you sure you want to delete\" dialog box").png "Clicking “Yes” on the “Are you sure you want to delete” dialog box")

    \
    The **Success – Deletion the App Set <**_**appset\_name**_**> has started** notification is shown and the App Set has a **Status** of **Deleting** whilst the App Set and it’s associated deployments are removed from the relevant companies.\


    ![Notification the App Set is being deleted](/_images/image-(2562 "Notification the App Set is being deleted").png "Notification the App Set is being deleted")

<blockquote class="wp-block-quote">
<p>**Note**</p>
<p>Deleting an App Set automatically deletes all of the deployments for all of the apps from all of the companies to which it was deployed. You don’t need to delete the individual deployments from the targeted companies before deleting the App Set.</p>
</blockquote>

Once the App Set has been successfully deleted (which can take an extended period of time depending on its contents and where it’s been deployed), the App Set will disappear from the **App Set** page.

!["App Set" page showing the App Set has been deleted](/_images/image-(2563 "\"App Set\" page showing the App Set has been deleted").png "“App Set” page showing the App Set has been deleted")