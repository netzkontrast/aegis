import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Exclude legacy apps from compilation
  typescript: {
    ignoreBuildErrors: false,
  },
  // Output standalone for deployment
  output: "standalone",
};

export default nextConfig;
