# Edit an MSP Custom App

_Applies to: Patch My PC Cloud_

To edit a Custom App for a Managed Service Provider (MSP) you’ve created in Patch My PC (PMPC) Cloud, follow the [Modify a Custom App](../../custom-apps/modify-a-custom-app.md) process for the relevant app.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>When you view the properties of a Custom App for an MSP, the <strong>Source</strong> field shows the name of the company that created the app.</p>
</blockquote>

You can also change:

* The visibility of the Custom App by selecting the new setting under the <strong>Custom App Visibility</strong> section of the <strong>Configurations</strong> page.
* Which child companies the app is visible on.

For example:

| Current setting         | New Setting        | Impact                                                                          |
| ----------------------- | ------------------ | ------------------------------------------------------------------------------- |
| No Customers            | All Customers      | Custom App will appear in the App Catalog of all child companies.               |
| No Customers            | Specific Customers | Custom App will only appear in the App Catalog of the selected child companies. |
| All /Specific Customers | No Customers       | Custom App will be removed from the App Catalog of all child companies.         |

<blockquote class="wp-block-quote">
<p><strong>Important</strong></p>
<p>If an app has been shared with and deployed from that company, changing either of the above settings may generate the "<strong>Are you sure?</strong>" popup warning you of the impact and asking you to confirm the deletion of the deployment of this app at the child company.</p>
<p>![“Are you sure” popup](/_images/image (344).png>)</p>
</blockquote>

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>If a child company has been selected in the <strong>Customers</strong> field, you cannot remove it if the app has been deployed from there. You must delete the deployment first, after which you can remove that child company from the list.</p>
</blockquote>