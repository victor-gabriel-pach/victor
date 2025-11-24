"use client"

import Editor from "@monaco-editor/react"

interface EditorProps {
  value?: string
  language?: string
  onChange?: (value: string | undefined) => void
}

export default function CodeEditor({ value = "", language = "python", onChange }: EditorProps) {
  return (
    <div className="w-full h-[calc(100vh-6rem)] py-2 px-2 border rounded-2xl overflow-hidden">
      <Editor
        height="100%"
        defaultLanguage={language}
        defaultValue={value}
        theme="vs-dark"
        onChange={onChange}
        options={{
          minimap: { enabled: false },
          fontSize: 14,
          lineNumbers: "on",
          scrollBeyondLastLine: false,
          automaticLayout: true,
        }}
      />
    </div>
  )
}
