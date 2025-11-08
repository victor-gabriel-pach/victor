"use client"
// @ts-ignore: side-effect CSS import (no types)
import "@/app/globals.css"
import { Provider } from "@/app/providers/providers"
import { Toaster } from "@/components/ui/sonner"

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="pt-BR" suppressHydrationWarning>
            <body className="min-h-screen bg-background font-sans antialiased">
                <Provider attribute="class" defaultTheme="system" enableSystem>
                    {children}
                    <Toaster />
                </Provider>
            </body>
        </html>
    )
}