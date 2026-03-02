import { NextRequest, NextResponse } from "next/server";
import { queryNcp, getNcpSections } from "@/lib/ncp";

export async function GET(request: NextRequest) {
  const path = request.nextUrl.searchParams.get("path");

  if (!path) {
    return NextResponse.json(
      { error: "Missing 'path' query parameter", sections: getNcpSections() },
      { status: 400 }
    );
  }

  if (path === "_sections") {
    return NextResponse.json({ sections: getNcpSections() });
  }

  const result = queryNcp(path);

  if (result === null || result === undefined) {
    return NextResponse.json(
      {
        error: `No data found at path: ${path}`,
        availableSections: getNcpSections(),
      },
      { status: 404 }
    );
  }

  return NextResponse.json({ path, result });
}
