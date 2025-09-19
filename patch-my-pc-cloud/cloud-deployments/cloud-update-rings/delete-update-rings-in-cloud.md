# Delete Update Rings in Cloud

_Applies to: Patch My PC Cloud_

For a Patch My PC (PMPC) Cloud deployment with Update Rings enabled, you can either:

* [Delete all Update Rings](delete-update-rings-in-cloud.md#delete-all-update-rings)
* [Delete a Single Update Ring](delete-update-rings-in-cloud.md#delete-a-single-update-ring)

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>All deletion tasks for Update Rings are performed from the <strong>Assignments</strong> tab of the respective deployment.</p>
</blockquote>

### Delete all Update Rings

To delete all Update Rings for a deployment:

1. [Edit](../manage-cloud-deployments/edit-a-cloud-deployment.md) the relevant deployment and navigate to the <strong>Assignments</strong> tab.
2.  If you want to delete a single Update Ring, use the [Delete a Single Update Ring](delete-update-rings-in-cloud.md#delete-a-single-update-ring) process.\
    \
    To delete all Update Rings for this deployment, click <strong>Remove all Rings</strong>.\


    ![Clicking “Remove all Rings”](/_images/image-(2061).png "Clicking “Remove all Rings”")


3.  On the <strong>Move Assignments or Delete</strong> dialog box, click <strong>Move</strong> to remove the Update Rings but keep all the existing assignments.\
    \


    ![Clicking “Move” to remove the Update Rings but keep all the existing assignments](/_images/image-(2062).png "Clicking “Move” to remove the Update Rings but keep all the existing assignments")

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Clicking <strong>Delete</strong> will delete any existing assignments but not the deployment itself.</p>
<p>![Clicking “Delete” will delete any existing assignments, not the deployment itself.](/_images/image-(2064).png>)\</p>
</blockquote>

The Update Rings are removed and any existing assignments are kept.

![Update Rings are removed and any existing assignments are kept](/_images/image-(2065).png "Update Rings are removed and any existing assignments are kept")

4.  Click <strong>Save</strong> to save your changes.\
    \


    ![Clicking “Save” to save changes](/_images/image-(2066).png "Clicking “Save” to save changes")

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>As removing all Update Rings disables Update Ring functionality for this deployment (which could result in unintended results), the <strong>"</strong>_<strong>\<deployment\_name></strong>_<strong>" Deployment Summary</strong> is shown detailing the impact of your proposed change.\</p>
<p>\</p>
<p>For example, this version of the app will be deployed immediately to all of the following assignments without any of the delays enforced by using Update Rings.</p>
<p>![“Deployment Summary” showing the impact of deleting all Update Rings ](/_images/image-(2067).png>)</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If the existing deployment had different versions applied to different assignments, we use the version that was applied to the lowest delay ring before the deployment was edited.</p>
</blockquote>

5.  Click <strong>Cancel</strong> to return to the <strong>Assignments</strong> tab to make any required changes, or click <strong>Confirm</strong> to save your changes.\
    \
    The <strong>Deployments</strong> node is displayed along with the <strong>Success – Edited <</strong>_<strong>deployment\_name</strong>_<strong>></strong> notification.\
    \


    ![“Deployment Summary” showing the impact of delete all Update Rings](/_images/image-(2068).png "“Deployment Summary” showing the impact of delete all Update Rings")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you edit the deployment and click <strong>More Info</strong>, you will see the tabs representing the Update Rings are no longer present.</p>
</blockquote>

### Delete a Single Update Ring

To delete a Single Update Ring:

1. Navigate to the <strong>Assignments</strong> page of the deployment.
2. Click the red <strong>X</strong> beside the Update Ring you want to delete.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>Deleting an Update Ring also deletes any assignments controlled by that ring. If you want to keep the assignment, drag and drop it to another ring before you delete the ring.</p>
</blockquote>

![Clicking the read “X” to delete a specific Update Ring](/_images/image-(2069).png "Clicking the read “X” to delete a specific Update Ring")

The ring and any assignments it contains are deleted.

![Update Ring deleted](/_images/image-(2070).png "Update Ring deleted")

3.  Click <strong>Save</strong> to save your changes.\
    \


    ![Clicking “Save” to save changes](/_images/image-(2071).png "Clicking “Save” to save changes")

    \
    As you’ve removed an Update Ring and it’s assignments, the <strong>"<</strong>_<strong>deployment\_name</strong>_<strong>>" Deployment Summary</strong> is shown detailing the impact of your proposed change.\
    \
    For example, by deleting the <strong>7-Zip Pilot +7 Days</strong> ring, this app will not be deployed to the <strong>03 - Patching - Production - All - 7 Days</strong> Entra ID group.\
    \


    ![“Deployment Summary” showing the impact of deleting this Update Rings](/_images/image-(2072).png "“Deployment Summary” showing the impact of deleting this Update Rings")
4.  Click <strong>Cancel</strong> to return to the <strong>Assignments</strong> tab to make any required changes, or click <strong>Confirm</strong> to save your changes.\
    \
    The <strong>Deployments</strong> node is displayed along with the <strong>Success – Edited <</strong>_<strong>deployment\_name</strong>_<strong>></strong> notification.\


    ![“Deployment Summary” showing the impact of delete all Update Rings](/_images/image-(2073).png "“Deployment Summary” showing the impact of delete all Update Rings")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you edit the deployment and click <strong>More Info</strong>, you will see the tab representing the deleted Update Ring is no longer present.</p>
</blockquote>