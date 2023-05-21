declare module "play" {
  type Options = {
    afplay?: string;
    mpg123?: string;
    mpg321?: string;
    play?: string;
    cmd?: string;
    executable?: string;
    args?: string[];
  };

  type Callback = (err?: Error) => void;

  class Player {
    constructor(options?: Options);
    play(sound: string, callback?: Callback): void;
    stop(callback?: Callback): void;
  }

  export = Player;
}
