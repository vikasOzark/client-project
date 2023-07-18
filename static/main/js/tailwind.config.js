tailwind.config = {
  theme: {
    extend: {
      colors: {
        success: 'rgb(34 197 94)',
        error: 'rgb(239 68 68)',
        warning: 'rgb(234 179 8)',
        success_light: 'rgb(34 197 94 / 15%)',
        error_light: 'rgb(239 68 68 / 15%)',
        warning_light: 'rgb(234 179 8 / 15%)',
      },
      backgroundImage: {
        'pattern': "url('./static/main/image/bg-grain-dark.png')",
      }
    }
  }
}