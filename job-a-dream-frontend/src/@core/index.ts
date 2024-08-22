import type { UserThemeConfig } from './types'
import type { LayoutConfig } from '@layouts/types'

export const defineThemeConfig = (userConfig: UserThemeConfig): { themeConfig: UserThemeConfig; layoutConfig: LayoutConfig } => {
  return {
    themeConfig: userConfig,
    layoutConfig: {
      app: {
        title: userConfig.app.title,
        logo: userConfig.app.logo,
        contentWidth: userConfig.app.contentWidth,
        contentLayoutNav: userConfig.app.contentLayoutNav,
        overlayNavFromBreakpoint: userConfig.app.overlayNavFromBreakpoint,

        iconRenderer: userConfig.app.iconRenderer,
      },
      navbar: {
        type: userConfig.navbar.type,
        navbarBlur: userConfig.navbar.navbarBlur,
      },
      footer: { type: userConfig.footer.type },
      horizontalNav: {
        type: userConfig.horizontalNav.type,
        transition: userConfig.horizontalNav.transition,
      },
      icons: {
        chevronDown: userConfig.icons.chevronDown,
        chevronRight: userConfig.icons.chevronRight,
        close: userConfig.icons.close,
        sectionTitlePlaceholder: userConfig.icons.sectionTitlePlaceholder,
      },
    },
  }
}
