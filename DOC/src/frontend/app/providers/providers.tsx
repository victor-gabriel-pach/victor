"use client"

import * as React from "react"
import { ThemeProvider } from "next-themes"
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

export function Provider({ children, ...props }: { children: React.ReactNode;[key: string]: any }) {
    const [queryClient] = React.useState(() => new QueryClient())
    return (
        <QueryClientProvider client={queryClient}>
            <ThemeProvider {...props}>
                {children}
            </ThemeProvider>
        </QueryClientProvider>
    )
}