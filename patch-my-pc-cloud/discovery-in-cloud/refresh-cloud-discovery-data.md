# Refresh Cloud Discovery Data

_Applies to: Patch My PC Cloud_

By default, you have to wait a week for the discovery data in your Patch My PC (PMPC) Cloud portal to refresh. Rather than waiting up to a week you can refresh the data in the Discovery node every 24 hours to pick up any changes.

To manually refresh the data in the <strong>Discovery</strong> node:

1. Navigate to the <strong>Discovery</strong> node.
2.  If the <strong>Refresh Data</strong> button is available, click it and go to Step 4.\


    ![“Refresh Data” button available](/_images/image-(394).png "“Refresh Data” button available")


3. If the <strong>Refresh Data</strong> button is unavailable, note the value of the <strong>Last Sync</strong> time.\
   \
   If it has been less than 24 hours since discovery last ran successfully, the <strong>Refresh Data</strong> button will be unavailable. Once 24 hours have passed, the <strong>Refresh Data</strong> button will be available.

<blockquote class="wp-block-quote">
<p><strong>Note</strong></p>
<p>The <strong>Last Sync</strong> time is the time when the last sync completed successfully, which is then converted to your local browser time and shown to you in the UI.</p>
</blockquote>

4.  The <strong>Refresh Data</strong> button changes to <strong>Collecting Data</strong> whilst discovery runs.\


    ![“Refresh Data” button changed to “Collecting Data” whilst discovery runs](/_images/image-(395).png "“Refresh Data” button changed to “Collecting Data” whilst discovery runs")
5. Currently, when the discovery process completes the portal does not auto-refresh. So periodically press <strong>F5</strong> to refresh the portal.
6.  Once discovery finishes running, the <strong>Last Sync</strong> time gets updated and the <strong>Refresh Data</strong> button becomes unavailable.\


    ![“Last Sync” time updated and “Refresh data” unavailable](/_images/image-(396).png "“Last Sync” time updated and “Refresh data” unavailable")

<blockquote class="wp-block-quote">
<p><strong>Tip</strong></p>
<p>If you look in the <strong>Events</strong> node, you will see the <strong>Intune Discovered Applications Refreshed</strong> event which is created whenever someone clicks <strong>Refresh Data</strong> to refresh your discovery data.</p>
</blockquote>