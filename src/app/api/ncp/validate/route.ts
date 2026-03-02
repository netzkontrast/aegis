import { NextRequest, NextResponse } from "next/server";
import { validateProse } from "@/lib/ncp";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { text, chapter } = body;

    if (!text || typeof text !== "string") {
      return NextResponse.json(
        { error: "Missing 'text' field (string)" },
        { status: 400 }
      );
    }

    const chapterNum =
      typeof chapter === "number" ? chapter : parseInt(chapter, 10) || 1;

    const result = validateProse(text, chapterNum);
    return NextResponse.json(result);
  } catch {
    return NextResponse.json(
      { error: "Invalid JSON body" },
      { status: 400 }
    );
  }
}

export async function GET() {
  return NextResponse.json({
    usage: "POST /api/ncp/validate with JSON body { text: string, chapter: number }",
    description:
      "Validates prose against NCP constraints including physics rules, style guidelines, and character presence.",
  });
}
