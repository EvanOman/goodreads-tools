# Release process

This repo uses release-please to automate version bumps and GitHub releases.
It keeps a single release PR open per branch and updates it as new conventional
commits land on `master`. You merge the release PR only when you want to cut a
release.

## Conventional commit format

Use conventional commit titles for PRs and squash-merge with the PR title:

```
feat: add reading timeline chart
fix: handle month-year start dates
chore: update CI workflows
```

Rules of thumb:

- `feat:` bumps minor.
- `fix:` bumps patch.
- `feat!:` or a `BREAKING CHANGE:` footer bumps major.

## Release flow

1) Merge feature PRs into `master` using squash merge with a conventional title.
2) Release-please opens or updates the release PR.
3) When ready, merge the release PR (squash merge is fine).
4) Release-please creates the tag and GitHub Release automatically.
5) The PyPI workflow runs on the GitHub Release. It will publish once OIDC is set up.
