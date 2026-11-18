// Unmount rendered components after each test (Testing Library does this itself only with vitest globals on).
import { cleanup } from "@testing-library/react";
import { afterEach } from "vitest";

afterEach(cleanup);
