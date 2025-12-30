frappe.pages["thunder-pos-setup"].on_page_load = function(wrapper) {
  const page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "Thunder POS Setup",
    single_column: true
  });

  $(page.body).html(`
    <div class="card">
      <div class="card-body">
        <h4>Quick Setup</h4>
        <ol>
          <li>Open <b>Neotec Thunder Settings</b> and configure outlet defaults.</li>
          <li>Create <b>Neotec Outlet</b> and <b>Neotec POS Profile</b>.</li>
          <li>(Restaurant) Setup Floors / Tables / Kitchen Stations.</li>
          <li>(Optional) Setup Offers / Loyalty / Web Ordering.</li>
        </ol>
        <p><b>Tip:</b> Use the global search (Ctrl+G) and type the DocType/Page name.</p>
      </div>
    </div>
  `);
};
