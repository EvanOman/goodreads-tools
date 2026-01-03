## Write-flow capture notes (in progress)

Goal: capture Goodreads write operations (shelve/rate/review) so we can implement authenticated POST requests safely.

### Tooling

- Use a browser you already use to access Goodreads (Chrome/Firefox/Safari).
- Open DevTools → Network tab.
- Ensure “Preserve log” is enabled to keep requests after navigation.

### Steps to capture

1. Navigate to a book page (e.g., `https://www.goodreads.com/book/show/44767458-dune`).
2. Trigger a write action:
   - Click **Want to Read** (default shelf).
   - Change shelf via the dropdown.
   - Add a rating.
   - Add a short review (optional).
3. In the Network tab, filter by `XHR`/`Fetch` and look for requests hitting `goodreads.com`.
4. For each relevant request, record:
   - HTTP method + URL
   - Query parameters
   - Request headers (especially `x-csrf-token`, `referer`, `content-type`)
   - Request payload (JSON or form)
   - Response status + response body

### Expected outputs

Create a note per action:

- **Shelve book**: endpoint, method, payload, response.
- **Rate book**: endpoint, method, payload, response.
- **Review book**: endpoint, method, payload, response.

Paste those findings into this doc and we’ll translate them into CLI commands.

### Safety notes

- Always run write commands with explicit confirmation.
- Keep a dry-run mode that prints the request and exits.
- Avoid bulk writes until we add rate limiting and error handling.
